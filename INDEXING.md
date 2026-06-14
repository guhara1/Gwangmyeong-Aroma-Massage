# 색인(인덱싱) 설정 가이드 — 네이버 · 구글 · 빙

빌드 시 자동 생성되는 색인 자산과, 검색엔진별 등록/통보 방법을 정리합니다.

## 빌드가 자동 생성하는 파일 (`python3 build.py`)

| 파일 | 위치 | 용도 |
|---|---|---|
| `sitemap.xml` | 루트 | 인덱싱 대상 14페이지 + `lastmod`/`priority` |
| `rss.xml` | 루트 | RSS 2.0 피드 (네이버·피드 수집기용, 전 페이지 `<link rel=alternate>` 연결) |
| `robots.txt` | 루트 | 크롤러 허용 + `Sitemap:` 2줄(sitemap, rss) |
| `{INDEXNOW_KEY}.txt` | 루트 | IndexNow 키 검증 파일 |

> 도메인은 `content/site.py`의 `BASE_URL`, IndexNow 키는 `INDEXNOW_KEY` 에서 관리합니다. 값을 바꾸면 다시 빌드만 하면 모든 파일에 반영됩니다.

## 1. 네이버 (가장 빠른 색인 경로)

1. **네이버 서치어드바이저** → 사이트 등록: `https://gwangmyeong-aroma-massage.pages.dev/`
2. 소유확인: **메인페이지에 인증 메타 태그가 이미 삽입**되어 있습니다(HTML 태그 방식).
3. **요청 → 사이트맵 제출**: `sitemap.xml`
4. **요청 → RSS 제출**: `rss.xml`
5. 네이버는 **IndexNow 참여사**이므로 아래 IndexNow 통보로도 즉시 반영됩니다.

## 2. 구글

1. **Google Search Console** → 속성 추가(URL 접두어 `https://gwangmyeong-aroma-massage.pages.dev/`)
2. 소유권 확인(HTML 태그/파일 중 택1 — 필요 시 메인에 메타 추가해 드립니다)
3. **색인 → Sitemaps**: `sitemap.xml` 제출
4. (선택) 즉시 통보가 필요하면 **Indexing API**: `tools/google_indexing.py` (구글은 IndexNow 미참여)

## 3. 빙(Bing)

1. **Bing Webmaster Tools** 등록(구글 SC에서 가져오기 가능) → `sitemap.xml` 제출
2. 빙은 IndexNow 참여사 → IndexNow 통보로 즉시 반영

## 4. IndexNow — 글 올릴 때마다 즉시 통보 (빙·네이버·얀덱스)

키 파일이 배포되어 있어야 합니다: `https://gwangmyeong-aroma-massage.pages.dev/ba53359ccbda0ad631943a07e70da14b.txt`

```bash
# 사이트맵 전체 제출
python3 tools/indexnow.py
# 특정 페이지만(권장: 글 1건 추가/수정 시)
python3 tools/indexnow.py https://gwangmyeong-aroma-massage.pages.dev/gwangmyeong/soha-dong-chuljangmassage/
```

### 자동화 (GitHub Actions)

`.github/workflows/indexnow.yml` — **main 브랜치 배포 시** 변경 사항을 감지해 IndexNow로 자동 통보합니다(배포 안정화를 위해 60초 대기 후 제출). 추가 시크릿 설정 없이 동작합니다.

## 참고: 사이트맵 핑(ping)에 대하여

구글·빙의 **사이트맵 핑 GET 엔드포인트(`/ping?sitemap=`)는 2023년 폐지**되었습니다. 따라서 자동화는 **IndexNow + Search Console/서치어드바이저 사이트맵 제출**로 구성하는 것이 현재 표준이며, 본 저장소도 그 방식으로 세팅되어 있습니다.
