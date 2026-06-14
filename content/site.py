# 사이트 공통 설정
BASE_URL = "https://gwangmyeong-aroma-massage.pages.dev"

BRAND = "간다GO"
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# 상단 메뉴 — 하위 메뉴에는 키워드를 반복하지 않고 지역명·역명만 표시한다.
# 대표 행정동·역세권 상위 항목은 메인 페이지의 해당 섹션 앵커로 연결한다.
NAV = [
    ("홈", "/", []),
    ("대표 행정동별 안내", "/#areas", [
        ("광명동", "/gwangmyeong/gwangmyeong-dong-chuljangmassage/"),
        ("철산동", "/gwangmyeong/cheolsan-dong-chuljangmassage/"),
        ("하안동", "/gwangmyeong/haan-dong-chuljangmassage/"),
        ("소하동", "/gwangmyeong/soha-dong-chuljangmassage/"),
        ("일직동", "/gwangmyeong/iljik-dong-chuljangmassage/"),
        ("학온동", "/gwangmyeong/hagon-dong-chuljangmassage/"),
    ]),
    ("역세권별 안내", "/#stations", [
        ("광명역", "/gwangmyeong/gwangmyeong-station-chuljangmassage/"),
        ("철산역", "/gwangmyeong/cheolsan-station-chuljangmassage/"),
        ("광명사거리역", "/gwangmyeong/gwangmyeongsageori-station-chuljangmassage/"),
    ]),
    ("예약안내", "/reservation/", [
        ("예약 방법", "/reservation/#how"),
        ("예약 가능 시간", "/reservation/#hours"),
        ("방문 가능 장소", "/reservation/#place"),
        ("결제·이동비 안내", "/reservation/#payment"),
        ("변경·취소 안내", "/reservation/#change"),
        ("예약 전 체크사항", "/reservation/#check"),
    ]),
    ("이용 전 확인사항", "/guide/", [
        ("처음 이용하시는 분", "/guide/#first"),
        ("방문 전 준비사항", "/guide/#prepare"),
        ("위생·안전 기준", "/guide/#hygiene"),
        ("관리 후 주의사항", "/guide/#after"),
        ("금지행위 안내", "/guide/#prohibited"),
        ("이용 FAQ", "/guide/#faq"),
    ]),
    ("홈타이 가이드", "/hometai/", [
        ("홈타이란 무엇인가", "/hometai/#what"),
        ("홈타이 이용 방법", "/hometai/#how"),
        ("추천 대상", "/hometai/#who"),
        ("출장마사지와의 차이", "/hometai/#diff"),
        ("자주 묻는 질문", "/hometai/#faq"),
    ]),
    ("고객센터", "/support/", [
        ("공지사항", "/support/#notice"),
        ("자주 묻는 질문", "/support/#faq"),
        ("1:1 문의", "/support/#contact"),
        ("제휴·기업 문의", "/support/#biz"),
        ("개인정보처리방침", "/privacy/"),
    ]),
]
