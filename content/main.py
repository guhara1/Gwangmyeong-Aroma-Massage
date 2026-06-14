# 메인 페이지 — 허브 역할. 모든 키워드를 밀어 넣지 않고 상세 페이지로 연결한다.
# 실제 오프라인 매장 주소가 없으므로 LocalBusiness Schema는 사용하지 않는다.
from .site import BASE_URL, BRAND, PHONE, PHONE_DISPLAY
from .pricing import PRICING

_JSONLD = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "{BRAND}",
  "url": "{BASE_URL}/",
  "telephone": "{PHONE}",
  "image": "{BASE_URL}/assets/og-image.png",
  "logo": "{BASE_URL}/assets/icon-512.png",
  "description": "광명시 전지역 방문 출장마사지·홈타이 예약 안내",
  "areaServed": {{
    "@type": "AdministrativeArea",
    "name": "경기도 광명시"
  }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "광명 출장마사지·광명시 홈타이 지역별 예약 안내",
  "url": "{BASE_URL}/",
  "description": "광명 출장마사지·홈타이 예약 전 대표 동, 역세권, 이용 기준을 정리했습니다.",
  "inLanguage": "ko-KR",
  "isPartOf": {{ "@type": "WebSite", "name": "{BRAND}", "url": "{BASE_URL}/" }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{ "@type": "ListItem", "position": 1, "name": "홈", "item": "{BASE_URL}/" }}
  ]
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "광명시 전지역 방문이 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "예약 시간, 정확한 위치, 배정 상황에 따라 달라집니다. 광명동·철산동·하안동·소하동·일직동·학온동 대표 행정동 페이지에서 동별 방문 조건을 확인할 수 있습니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "광명역이나 철산역 근처도 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "광명역, 철산역, 광명사거리역 역세권은 각 역 안내 페이지에서 주변 생활권과 함께 정리했습니다. 정확한 가능 여부는 예약 시 위치 기준으로 확인합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "광명1동, 철산2동처럼 번호가 붙은 동은 왜 따로 없나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "광명1~7동, 철산1~4동, 하안1~4동, 소하1~2동은 각각 광명동·철산동·하안동·소하동 대표 페이지에서 통합 안내해 중복 페이지 위험을 줄였습니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "홈타이와 출장마사지는 다른 건가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "홈타이는 자택·숙소·사무실 인근에서 받는 방문형 관리 서비스의 한 형태입니다. 자세한 내용은 홈타이 이용 가이드에서 확인할 수 있습니다."
      }}
    }}
  ]
}}
</script>
"""

_HERO = f"""<section class="hero">
  <div class="hero-inner">
    <p class="hero-badge">Premium Visiting Spa · 광명시 전지역</p>
    <h1>광명 출장마사지·광명시 홈타이<br>지역별 예약 안내</h1>
    <p class="hero-lead">샵까지 갈 필요 없이, 계신 곳에서 받는 방문 관리.<br>자택·오피스텔·숙소 어디든 전화 한 통이면 예약이 끝납니다.</p>
    <div class="hero-actions">
      <a class="hero-btn primary" href="tel:{PHONE}">📞 {PHONE_DISPLAY}</a>
      <a class="hero-btn" href="#areas">대표 행정동 안내 보기</a>
    </div>
    <ul class="hero-stats">
      <li><strong>6개</strong><span>대표 행정동</span></li>
      <li><strong>3개</strong><span>역세권 안내</span></li>
      <li><strong>전지역</strong><span>방문 가능</span></li>
      <li><strong>24시간</strong><span>예약 상담</span></li>
    </ul>
  </div>
</section>
"""

_BODY = f"""
<section id="reason">
<h2>광명시에서 출장마사지를 찾는 이유</h2>
<p>광명 출장마사지를 찾는 분들은 대부분 현재 위치에서 가까운 방문 가능 지역을 먼저 확인합니다. 광명시는 서울 서남권과 맞닿아 있어 이동 수요가 많고, 광명동·철산동·하안동·소하동·일직동·학온동처럼 생활권이 비교적 뚜렷하게 나뉘는 지역입니다. 그래서 이 광명시 홈타이 안내 사이트는 단순히 예약 문구만 보여주는 방식보다, 사용자가 본인 위치에 맞는 지역과 역세권을 쉽게 찾을 수 있도록 구성했습니다. 이 페이지는 광명시 전체 구조를 설명하는 허브이며, 더 자세한 내용은 대표 행정동별·역세권별 안내 페이지에서 확인하실 수 있습니다.</p>
<p>광명시 안내에서 가장 중요한 기준은 대표 행정동 통합입니다. 광명1동부터 광명7동까지 각각 페이지를 만들면 페이지 수는 많아지지만 내용이 거의 비슷해질 가능성이 큽니다. 철산1동부터 철산4동, 하안1동부터 하안4동, 소하1동과 소하2동도 같은 문제가 생길 수 있습니다. 따라서 광명동·철산동·하안동·소하동처럼 대표 지역 1개 페이지로 묶고, 본문 안에서 세부 생활권을 자연스럽게 설명하는 방식이 안전합니다. 번호가 붙은 행정동으로 검색해 들어오셨더라도 필요한 내용은 모두 대표 동 페이지 안에 있습니다.</p>
</section>

<section id="hometai">
<h2>광명 홈타이 이용 전 확인할 사항</h2>
<p>광명 홈타이는 자택, 숙소, 사무실 인근에서 예약 가능 여부를 먼저 확인한 뒤 이용하는 방문형 관리 서비스입니다. 출장마사지가 처음이라면 방문 가능 지역, 관리 가능 시간, 추가 이동비, 결제 방식, 취소 기준, 서비스 범위를 미리 확인해 두시면 통화가 한결 짧고 정확해집니다. 홈타이는 오일을 쓰지 않고 편한 옷차림으로 받는 지압·스트레칭 구성이라 샤워 부담이 적어 처음 이용하는 분들이 시작하기 좋습니다. 관리 방식과 추천 대상은 <a href="/hometai/">홈타이 이용 가이드</a>에서, 방문 전 준비사항은 <a href="/guide/">이용 전 확인사항</a>에서 정리해 두었습니다.</p>
</section>

<section id="areas">
<h2>대표 행정동별 방문 가능 지역 안내</h2>
<p>광명시 지역 안내는 광명동·철산동·하안동·소하동·일직동·학온동 여섯 개 대표 행정동을 중심으로 구성됩니다. 각 페이지에서는 해당 생활권의 특징, 가까운 역세권, 방문 전 확인사항, 예약 가능 시간을 동마다 고유한 내용으로 설명합니다. 아래에서 거주하시거나 머무시는 동을 선택해 주세요.</p>
<ul class="card-grid">
<li><a href="/gwangmyeong/gwangmyeong-dong-chuljangmassage/">광명동 출장마사지</a></li>
<li><a href="/gwangmyeong/cheolsan-dong-chuljangmassage/">철산동 출장마사지</a></li>
<li><a href="/gwangmyeong/haan-dong-chuljangmassage/">하안동 출장마사지</a></li>
<li><a href="/gwangmyeong/soha-dong-chuljangmassage/">소하동 출장마사지</a></li>
<li><a href="/gwangmyeong/iljik-dong-chuljangmassage/">일직동 출장마사지</a></li>
<li><a href="/gwangmyeong/hagon-dong-chuljangmassage/">학온동 출장마사지</a></li>
</ul>
<p>광명동은 광명사거리역과 광명전통시장 중심의 오래된 상권·주거 생활권, 철산동은 철산역과 광명시청 인근 상업·주거 지역입니다. 하안동은 대규모 아파트 단지와 하안사거리 생활권, 소하동은 소하상업지구와 업무·주거 수요가 함께 있는 지역입니다. 일직동은 KTX 광명역과 대형 쇼핑시설·업무 수요가 모인 역세권이고, 학온동은 가학·노온사·옥길 생활권으로 차량 이동 기준이 더 중요한 지역입니다. 같은 광명시라도 동마다 주거 형태와 생활 리듬이 달라, 방문 시간대나 이동 동선 안내도 동별로 조금씩 다릅니다.</p>
</section>

<section id="stations">
<h2>광명역·철산역·광명사거리역 역세권 안내</h2>
<p>역세권 페이지는 광명 지역 검색에서 중요한 역할을 합니다. 광명역 출장마사지, 철산역 출장마사지, 광명사거리역 출장마사지처럼 실제 검색어와 가까운 기준으로 안내하되, 같은 역을 교통수단별로 나눠 중복 페이지를 만들지 않습니다. 광명역은 KTX와 수도권 이동 수요가 함께 있지만 페이지는 하나만 두고 본문 안에서 교통 특징을 설명합니다.</p>
<ul class="card-grid">
<li><a href="/gwangmyeong/gwangmyeong-station-chuljangmassage/">광명역 출장마사지</a></li>
<li><a href="/gwangmyeong/cheolsan-station-chuljangmassage/">철산역 출장마사지</a></li>
<li><a href="/gwangmyeong/gwangmyeongsageori-station-chuljangmassage/">광명사거리역 출장마사지</a></li>
</ul>
<p>광명역은 일직동 업무·쇼핑 생활권과 KTX 이용 수요를, 철산역은 철산동 중심 상권을, 광명사거리역은 광명동 생활권을 대표합니다. 역 이름으로 위치를 설명하는 것이 편하시면 각 역 페이지를, 거주 지역 기준이 편하시면 대표 행정동 페이지를 참고하시면 됩니다. 어느 쪽을 보셔도 예약 절차와 이용 기준은 같습니다.</p>
</section>

<section id="reserve">
<h2>예약 전 꼭 확인해야 할 기준</h2>
<p>예약 전에는 방문 가능 지역, 관리 가능 시간, 추가 이동비, 결제 방식, 취소 기준, 서비스 범위를 먼저 확인해야 합니다. 광명시는 광명동·철산동처럼 역세권 중심 지역도 있고, 일직동·학온동처럼 차량 이동 기준이 더 중요한 지역도 있습니다. 사용자가 불편을 겪지 않도록 <a href="/reservation/">예약안내</a> 페이지에서 주소 확인, 예약 가능 시간, 방문 전 확인사항을 명확하게 정리했습니다. 정확한 도로명 주소와 희망 시간대만 정해 두시면 예약 통화는 1~2분 안에 끝납니다.</p>
</section>

<section id="guide">
<h2>광명 출장마사지 사이트 이용 가이드</h2>
<p>이 사이트의 모든 문구는 과장된 표현보다 신뢰를 주는 안내형 문장으로 구성했습니다. 불법 서비스, 선정적인 표현, 허위 후기, 과도한 할인 문구는 사용하지 않습니다. 정상적인 방문 관리 안내 사이트로서 이용 가능 지역, 예약 절차, 취소 기준, 개인정보 처리 기준, 고객 유의사항을 분명하게 보여드립니다. 메인 페이지는 광명시 전체 안내를 담당하고, 대표 행정동 페이지는 광명동·철산동·하안동·소하동·일직동·학온동 검색을, 역세권 페이지는 광명역·철산역·광명사거리역 검색을 담당합니다. 처음이라면 <a href="/guide/">이용 전 확인사항</a>과 <a href="/hometai/">홈타이 이용 가이드</a>를 먼저 읽어보시길 권합니다.</p>
</section>

<section id="faq">
<h2>자주 묻는 질문</h2>
<div class="faq-item">
<h3>광명시 전지역 방문이 가능한가요?</h3>
<p>예약 시간, 정확한 위치, 배정 상황에 따라 달라집니다. 광명동, 철산동, 하안동, 소하동, 일직동, 학온동 대표 행정동 페이지에서 동별 방문 조건을 확인할 수 있습니다.</p>
</div>
<div class="faq-item">
<h3>광명역이나 철산역 근처도 가능한가요?</h3>
<p>광명역, 철산역, 광명사거리역 역세권은 각 역 안내 페이지에서 주변 생활권과 함께 정리했습니다. 정확한 가능 여부는 예약 시 위치 기준으로 확인합니다.</p>
</div>
<div class="faq-item">
<h3>광명1동, 철산2동처럼 번호가 붙은 동은 왜 따로 없나요?</h3>
<p>광명1~7동, 철산1~4동, 하안1~4동, 소하1~2동은 각각 광명동·철산동·하안동·소하동 대표 페이지에서 통합 안내해 중복 페이지 위험을 줄였습니다.</p>
</div>
<div class="faq-item">
<h3>홈타이와 출장마사지는 다른 건가요?</h3>
<p>홈타이는 자택·숙소·사무실 인근에서 받는 방문형 관리 서비스의 한 형태입니다. 자세한 내용은 <a href="/hometai/">홈타이 이용 가이드</a>에서 확인할 수 있습니다.</p>
</div>
</section>

{PRICING}
<section id="contact" class="cta">
<h2>예약문의</h2>
<p>광명시 방문 관리 예약과 상담은 전화로 가장 빠르게 진행됩니다. 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

PAGE = {
    "path": "",
    "title": "광명 출장마사지｜광명시 홈타이 지역별 예약 안내",
    "desc": "광명 출장마사지·홈타이 예약 전 대표 동, 역세권, 이용 기준을 정리했습니다.",
    "h1": "광명 출장마사지 · 광명시 홈타이 지역별 예약 안내",
    "body": _BODY,
    "extra_head": _JSONLD,
    "breadcrumb": [],
    "hero": _HERO,
}
