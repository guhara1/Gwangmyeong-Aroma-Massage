# 간다GO — 광명 출장마사지 · 광명시 홈타이 지역 SEO 사이트

경기도 광명시 전지역 방문형 마사지(출장마사지)·홈타이 예약 안내를 위한 정적 사이트입니다.
`content/` 패키지의 페이지 정의를 `build.py` 가 읽어 정적 HTML을 생성합니다.

- 상호: **간다GO**
- 예약 전화: **0508-202-4719**
- 핵심 키워드: 출장마사지 / 보조 키워드: 홈타이

## 사이트 구조 (총 15페이지)

```
메인 (/)
├ 대표 행정동 (6)
│  ├ 광명동   /gwangmyeong/gwangmyeong-dong-chuljangmassage/
│  ├ 철산동   /gwangmyeong/cheolsan-dong-chuljangmassage/
│  ├ 하안동   /gwangmyeong/haan-dong-chuljangmassage/
│  ├ 소하동   /gwangmyeong/soha-dong-chuljangmassage/
│  ├ 일직동   /gwangmyeong/iljik-dong-chuljangmassage/
│  └ 학온동   /gwangmyeong/hagon-dong-chuljangmassage/
├ 역세권 (3)
│  ├ 광명역       /gwangmyeong/gwangmyeong-station-chuljangmassage/
│  ├ 철산역       /gwangmyeong/cheolsan-station-chuljangmassage/
│  └ 광명사거리역  /gwangmyeong/gwangmyeongsageori-station-chuljangmassage/
└ 안내 (5)
   ├ 예약안내          /reservation/
   ├ 이용 전 확인사항    /guide/
   ├ 홈타이 이용 가이드  /hometai/
   ├ 고객센터          /support/
   └ 개인정보처리방침    /privacy/  (noindex)
```

## SEO 원칙 (구글 가이드라인 준수)

- **중복 방지**: 광명1~7동·철산1~4동·하안1~4동·소하1~2동 등 번호 행정동은 대표 동 1페이지로 통합.
- **역세권 단일 페이지**: 교통수단별 중복 URL을 만들지 않고 역당 1페이지.
- **키워드 자연 배치**: 출장마사지는 Title·H1·본문 핵심 위치에, 홈타이는 보조 설명형 문장에 배치(반복 남용 금지).
- **메타 description 80자 이내** 공통 적용.
- **Schema**: Organization / WebPage / BreadcrumbList / FAQPage. 오프라인 매장 주소가 없어 LocalBusiness는 사용하지 않음.
- 본문 2,000자 미만 페이지는 `build.py` 가 자동으로 `noindex` 처리하고 sitemap에서 제외.

## 빌드

```bash
python3 build.py
```

`sitemap.xml`, `rss.xml`, `robots.txt`, IndexNow 키 파일, `.nojekyll` 가 자동 생성됩니다. Cloudflare Pages 등 정적 호스팅에 그대로 배포할 수 있습니다.

## 색인(인덱싱)

네이버·구글·빙 등록과 IndexNow 즉시 통보 설정은 [INDEXING.md](INDEXING.md) 를 참고하세요.
- `python3 tools/indexnow.py` — 빙·네이버·얀덱스 즉시 통보(키 파일 기반)
- `python3 tools/google_indexing.py` — 구글 Indexing API(서비스 계정 필요)
- `.github/workflows/indexnow.yml` — main 배포 시 IndexNow 자동 통보

## 배포 전 설정

- `content/site.py` 의 `BASE_URL` 을 실제 도메인으로 변경 후 다시 빌드하세요. (canonical·og·sitemap에 반영됩니다.)
