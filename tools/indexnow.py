#!/usr/bin/env python3
"""IndexNow 즉시 색인 통보 스크립트.

빙(Bing)·네이버(Naver)·얀덱스(Yandex) 등 IndexNow 참여 검색엔진에
변경된 URL을 한 번의 요청으로 통보한다. (구글은 IndexNow 미참여 → tools/google_indexing.py 사용)

사용법:
  python3 tools/indexnow.py                # sitemap.xml 의 전체 URL 제출
  python3 tools/indexnow.py URL [URL ...]  # 지정한 URL만 제출 (글 1건 올렸을 때 권장)

키는 content/site.py 의 INDEXNOW_KEY 를 사용하며, 사이트 루트의
{KEY}.txt 파일이 배포되어 있어야 검증을 통과한다.
"""
import json
import os
import re
import sys
import urllib.request
import urllib.error

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content.site import BASE_URL, INDEXNOW_KEY  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = BASE_URL.rstrip("/")
HOST = re.sub(r"^https?://", "", BASE)
# api.indexnow.org 는 참여 엔진 전체로 전달한다.
ENDPOINT = "https://api.indexnow.org/indexnow"


def sitemap_urls():
    path = os.path.join(ROOT, "sitemap.xml")
    with open(path, encoding="utf-8") as f:
        return re.findall(r"<loc>([^<]+)</loc>", f.read())


def submit(urls):
    urls = [u for u in urls if u.startswith(BASE)]
    if not urls:
        print("제출할 URL이 없습니다.")
        return 1
    payload = {
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": f"{BASE}/{INDEXNOW_KEY}.txt",
        "urlList": urls,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT, data=data,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    print(f"IndexNow 제출 → {ENDPOINT}")
    print(f"  host={HOST}  키파일={BASE}/{INDEXNOW_KEY}.txt")
    for u in urls:
        print(f"  - {u}")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            print(f"응답: {resp.status} {resp.reason}")
            # 200/202 = 정상 접수
            return 0 if resp.status in (200, 202) else 2
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "ignore")
        print(f"HTTP 오류 {e.code}: {body}")
        return 2
    except urllib.error.URLError as e:
        print(f"네트워크 오류: {e.reason}")
        return 2


if __name__ == "__main__":
    args = sys.argv[1:]
    targets = args if args else sitemap_urls()
    raise SystemExit(submit(targets))
