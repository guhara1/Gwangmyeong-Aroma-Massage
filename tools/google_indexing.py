#!/usr/bin/env python3
"""구글 Indexing API 즉시 색인 통보 스크립트.

구글은 IndexNow에 참여하지 않으므로, 즉시 통보가 필요할 때 이 스크립트를 사용한다.
(일반 페이지에 대한 Indexing API 사용은 공식적으로는 JobPosting/BroadcastEvent 대상이지만,
 실무에서 URL 색인 요청 용도로 널리 쓰인다. 정식 색인 경로는 Search Console 사이트맵 제출이다.)

준비물:
  1) Google Cloud 프로젝트에서 "Indexing API" 사용 설정
  2) 서비스 계정 생성 → JSON 키 발급
  3) Search Console 속성에 그 서비스 계정 이메일을 "소유자(Owner)"로 추가
  4) pip install google-auth

사용법:
  export GOOGLE_APPLICATION_CREDENTIALS=/path/service-account.json
  python3 tools/google_indexing.py                # sitemap.xml 전체 URL 통보
  python3 tools/google_indexing.py URL [URL ...]  # 지정 URL만 통보
  python3 tools/google_indexing.py --delete URL   # 삭제(URL_DELETED) 통보
"""
import json
import os
import re
import sys
import urllib.request
import urllib.error

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from content.site import BASE_URL  # noqa: E402

BASE = BASE_URL.rstrip("/")
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
SCOPES = ["https://www.googleapis.com/auth/indexing"]


def sitemap_urls():
    with open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8") as f:
        return re.findall(r"<loc>([^<]+)</loc>", f.read())


def get_token():
    try:
        from google.oauth2 import service_account
        import google.auth.transport.requests as gar
    except ImportError:
        sys.exit("google-auth 가 필요합니다:  pip install google-auth")
    cred_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not cred_path or not os.path.exists(cred_path):
        sys.exit("환경변수 GOOGLE_APPLICATION_CREDENTIALS 에 서비스계정 JSON 경로를 지정하세요.")
    creds = service_account.Credentials.from_service_account_file(cred_path, scopes=SCOPES)
    creds.refresh(gar.Request())
    return creds.token


def notify(url, token, deleted=False):
    body = json.dumps({
        "url": url,
        "type": "URL_DELETED" if deleted else "URL_UPDATED",
    }).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT, data=body, method="POST",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            print(f"  {resp.status} {url}")
            return resp.status == 200
    except urllib.error.HTTPError as e:
        print(f"  ERR {e.code} {url}: {e.read().decode('utf-8','ignore')}")
        return False


if __name__ == "__main__":
    args = sys.argv[1:]
    deleted = "--delete" in args
    args = [a for a in args if a != "--delete"]
    targets = args if args else sitemap_urls()
    targets = [u for u in targets if u.startswith(BASE)]
    if not targets:
        sys.exit("제출할 URL이 없습니다.")
    token = get_token()
    print(f"구글 Indexing API 통보 ({'삭제' if deleted else '갱신'}) — {len(targets)}건")
    ok = sum(notify(u, token, deleted) for u in targets)
    print(f"완료: {ok}/{len(targets)} 성공")
    raise SystemExit(0 if ok == len(targets) else 2)
