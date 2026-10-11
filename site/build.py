"""Build static support and privacy pages. No dependencies or visitor analytics."""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).parent
OUT = ROOT.parent / 'docs'
BASE = '/moneywaves-support'
EMAIL = 'it@bebriz.com'
OWNER = 'Deokjoo Moon'
CONTENT = {
 'ko': {
  'brand':'돈결', 'support':'지원', 'privacy':'개인정보처리방침',
  'tag':'돈의 흐름을 차분하게.', 'intro':'수입·지출부터 예산과 영수증까지. 돈결을 사용하는 데 필요한 안내와 문의 방법을 확인하세요.',
  'contact':'도움이 필요하신가요?', 'contactText':'앱 버전, iOS 버전과 문제를 재현하는 방법을 알려주세요. 스크린샷에서는 계좌명·금액·영수증 등 민감한 정보를 가려주세요. 장부 백업이나 결제 비밀번호를 보내지 마세요.',
  'mail':'이메일로 문의하기', 'faq':'자주 묻는 질문',
  'questions':[
   ('장부는 어디에 저장되나요?', '장부와 첨부한 영수증은 기기에 저장됩니다. 회원가입이나 은행 계좌 연동 없이 사용할 수 있으며, 개발자의 서버로 장부를 업로드하지 않습니다.'),
   ('기기를 바꾸기 전에 무엇을 해야 하나요?', '더보기의 백업·복원 화면에서 사진을 포함한 백업 파일을 내보내고 안전하게 보관하세요. 새 기기에서 해당 파일을 선택해 복원하세요. 복원은 현재 장부를 교체하므로 먼저 현재 장부도 백업하세요. 자동 동기화나 자동 백업 기능은 없습니다.'),
   ('Premium은 구독인가요?', 'Premium은 배너 광고를 제거하는 선택 사항인 일회성 인앱 구매입니다. 모든 가계부 기능은 무료이며, 구매 기능은 iOS 15 이상에서 사용할 수 있습니다. 가격은 Apple이 제공하는 구매 화면에서 확인하세요.'),
   ('구매했는데 광고가 보여요.', '구매할 때 사용한 Apple 계정으로 App Store에 로그인한 뒤 더보기 → 광고 제거 → 구매 복원을 실행하세요. 인터넷 연결을 확인하고 계속 문제가 있으면 문의해 주세요. 환불은 Apple에서 처리합니다.'),
   ('가격을 불러오지 못했다고 나와요.', '인터넷 연결을 확인하고 프리미엄 화면에서 다시 시도하세요. App Store 상품 제공 상태에 따라 조회가 실패할 수 있습니다. 계속 실패하면 앱 버전과 발생 시점을 적어 문의해 주세요. 가격을 확인할 수 없는 상태에서는 구매를 시작하지 않습니다.'),
   ('광고가 표시되지 않아요.', '광고는 인터넷 연결, 동의 상태와 광고 제공 여부에 따라 표시되지 않을 수 있습니다. 광고가 없어도 장부 기능을 사용할 수 있습니다. 개인정보 선택 버튼은 광고 SDK가 요구하는 경우 배너 영역에 표시됩니다.'),
   ('통화를 바꾸면 환율이 적용되나요?', 'KRW·USD·JPY 표시와 입력 단위를 지원하며, 자동 환율 변환이나 여러 통화 합산 기능은 아닙니다. 장부에 기록한 금액과 백업을 확인한 뒤 통화 설정을 변경하세요.'),
   ('데이터를 삭제하거나 접근 권한을 바꾸려면?', '거래와 첨부 사진은 앱에서 관리할 수 있습니다. 앱을 삭제하면 기기의 앱 데이터가 제거되며, 내보낸 백업이나 별도로 저장한 사진은 해당 저장 위치에서 직접 삭제해야 합니다. 카메라·사진 권한은 iOS 설정에서 변경할 수 있습니다.')],
  'policyIntro':'이 방침은 Deokjoo Moon이 제공하는 돈결(MoneyWaves) iOS 앱과 이 지원 웹사이트에 적용됩니다.',
  'effective':'최종 업데이트: 2026년 10월 11일',
  'sections':[
   ('기기에 저장하는 정보', '앱은 거래의 날짜·금액·유형·분류·계좌·메모, 예산과 반복 일정, 카드 설정, 첨부한 영수증 사진 및 앱 설정을 기기에 저장합니다. 앱 계정을 만들지 않으며 은행 로그인 정보를 요청하지 않습니다. 개발자는 장부와 사진을 서버로 수집하거나 열람하지 않습니다.'),
   ('사진과 파일 백업', '카메라와 사진 접근은 사용자가 영수증을 촬영하거나 사진을 선택할 때 이용합니다. 앱이 관리하는 iOS 장부·사진 폴더는 OS 자동 백업에서 제외하도록 설정되어 있습니다. 사용자가 직접 내보낸 백업에는 장부와 첨부 사진이 포함되며, 선택한 저장 위치나 공유 앱의 정책에 따라 처리됩니다. 백업 파일과 별도로 저장한 사진은 사용자가 관리하고 삭제해야 합니다.'),
   ('광고와 Google AdMob', '무료 버전은 Google Mobile Ads SDK와 동의 관리 SDK를 사용합니다. SDK는 광고 제공, 측정, 진단 및 부정행위 방지를 위해 IP 주소와 이를 통한 대략적 위치, 앱·기기 식별자, 광고 및 사용자 상호작용 정보, 충돌·성능 등 진단 정보를 처리할 수 있습니다. 수집 항목과 보관은 Google의 정책, SDK 설정과 사용자 선택에 따라 달라집니다. 장부 내용과 영수증 사진은 광고 요청에 첨부하지 않습니다. 앱은 비개인화 광고를 요청하지만, 비개인화 광고도 기술 정보를 처리할 수 있습니다. 앱은 ATT 추적 권한 요청을 표시하지 않습니다. 필요한 지역에서는 Google 동의 화면을 제공하며, SDK가 요구할 때 개인정보 선택 버튼을 통해 선택을 변경할 수 있습니다. 검증된 Premium 권한이 있으면 앱의 배너 광고 요청을 중단합니다.'),
   ('Apple 결제와 구매 복원', 'Premium 구매는 Apple StoreKit으로 처리합니다. Apple은 결제 및 계정 정보를 처리하며, 개발자는 카드번호나 결제 비밀번호를 받지 않습니다. 앱은 상품 가격과 검증된 구매 권한을 확인해 광고 제거를 적용합니다. 구매·환불·복원과 Apple의 보관은 Apple 정책을 따릅니다.'),
   ('업데이트 확인과 리뷰 요청', '앱은 업데이트 확인을 위해 Apple의 공개 조회 서비스 또는 GitHub에 호스팅된 공개 TestFlight 배포 정보를 조회합니다. 요청은 앱 식별자와 국가 등 조회 조건을 포함할 수 있고, 서비스 제공자는 IP 주소 등의 연결 정보를 처리할 수 있습니다. 이 요청에 장부·영수증이나 별도 생성한 사용자 식별자를 첨부하지 않습니다. 최초 사용일, 리뷰 요청 시점과 업데이트 안내 이력은 기기에 저장하며, 리뷰 화면 표시와 사용자가 제출한 리뷰는 Apple에서 처리합니다.'),
   ('지원 문의와 웹사이트', '사용자가 이메일로 문의하면 이메일 주소와 사용자가 보내는 문의 내용을 지원 응대에 사용합니다. 민감한 장부·영수증 정보는 보내지 마세요. 문의 정보는 응대와 필요한 기록 관리 기간 동안 처리하며, 삭제 요청은 아래 연락처로 보내주세요. 이 웹사이트에는 별도의 분석 도구, 광고, 추적 쿠키나 문의 입력 폼을 설치하지 않았습니다. 호스팅 제공자는 페이지 제공과 보안을 위해 IP 주소와 요청 정보 등 접속 로그를 처리할 수 있습니다.'),
   ('보관·삭제 및 선택', '장부와 사진은 사용자가 삭제하거나 앱을 삭제할 때까지 기기에 남습니다. 삭제한 자료의 사본이 백업 파일이나 다른 저장 위치에 있으면 그 사본도 별도로 삭제하세요. 기기 잠금과 안전한 백업 보관을 권장합니다. 카메라·사진 권한을 변경하고, 제공되는 광고 동의 선택을 조정하거나, 개인정보 관련 문의와 삭제 요청을 보낼 수 있습니다. Google·Apple·호스팅·메일 서비스가 처리하는 정보는 각 제공자의 정책과 보관 기준도 적용됩니다.'),
   ('해외 처리와 방침 변경', '광고, 결제, 호스팅 및 이메일 제공자의 서비스 운영에 따라 기술 정보나 문의 정보가 사용자의 국가 밖에서 처리될 수 있습니다. 앱의 처리 방식이 달라지면 이 페이지의 방침과 업데이트 날짜를 변경합니다.'),
   ('개인정보 문의', '운영자: Deokjoo Moon. 지원 및 개인정보 문의: it@bebriz.com.')],
  'providers':'외부 서비스 정책', 'footer':'장부는 기기에, 도움은 가까이에.'
 },
 'en': {
  'brand':'MoneyWaves', 'support':'Support', 'privacy':'Privacy policy',
  'tag':'A calmer view of your money.', 'intro':'Help with your ledger, budgets, receipts and optional Premium purchase.',
  'contact':'Need a hand?', 'contactText':'Include your app version, iOS version and steps to reproduce the issue. Hide account names, amounts and receipt details in screenshots. Do not send ledger backups or payment passwords.',
  'mail':'Contact support', 'faq':'Frequently asked questions',
  'questions':[
   ('Where is my ledger stored?', 'Your ledger and attached receipt photos are stored on your device. No app account or bank connection is required, and your ledger is not uploaded to a developer server.'),
   ('How do I move to a new device?', 'Export a backup, including photos, from More → Backup and Restore. Keep it safe and restore the file on your new device. Restoring replaces the current ledger, so back it up first. There is no automatic synchronization or automatic backup feature.'),
   ('Is Premium a subscription?', 'Premium is an optional one-time in-app purchase that removes banner ads. All ledger features remain free. Purchases require iOS 15 or later. Apple provides the price shown on the purchase screen.'),
   ('I purchased Premium but still see ads.', 'Sign in to the App Store with the Apple Account used to purchase, then open More → Remove Ads → Restore Purchases. Check your internet connection. Contact support if the issue continues. Apple handles refunds.'),
   ('Why is the price unavailable?', 'Check your internet connection and retry on the Premium screen. Product availability from the App Store can affect requests. If it persists, contact support with your app version and the time of the issue. The app does not start a purchase without a loaded price.'),
   ('Why are no ads showing?', 'Ads depend on connectivity, consent and ad availability. Ledger features remain usable without ads. A privacy choices button appears in the banner area when required by the advertising SDK.'),
   ('Does changing currency convert my money?', 'USD, KRW and JPY display and input units are supported. This does not perform exchange-rate conversion or combine multiple currencies. Check your ledger amounts and backups before changing currency.'),
   ('How do I delete data or change permissions?', 'Manage entries and attachments in the app. Deleting the app removes its device data. Delete exported backups and separately saved photos from their own storage locations. Camera and photo permissions can be changed in iOS Settings.')],
  'policyIntro':'This policy covers the MoneyWaves iOS app and this support website, provided by Deokjoo Moon.',
  'effective':'Last updated: October 11, 2026',
  'sections':[
   ('Information stored on your device', 'The app stores entry dates, amounts, types, categories, accounts and notes, budgets, recurring schedules, card settings, receipt photos and app preferences on your device. It does not create app accounts or request bank login credentials. The developer does not collect or view your ledger or photos through a server.'),
   ('Photos and file backups', 'Camera and photo access is used when you take or select receipt photos. The iOS ledger and photo folder managed by the app is configured to be excluded from automatic OS backups. A backup you export includes your ledger and attached photos; its handling depends on the storage location or sharing app you choose. You manage and delete exported backups and separately saved photos.'),
   ('Advertising and Google AdMob', 'The free version uses the Google Mobile Ads SDK and consent management SDK. They may process IP addresses and approximate location inferred from them, app or device identifiers, advertising and interaction information, and crash or performance diagnostics for advertising, measurement, diagnostics and fraud prevention. Collection and retention depend on Google policies, SDK configuration and your choices. Ledger contents and receipt photos are not attached to ad requests. The app requests non-personalized ads, which may still process technical data. The app does not display an ATT tracking permission request. Google consent forms are provided where required, and a privacy choices button is available when required by the SDK. Verified Premium ownership stops banner ad requests from the app.'),
   ('Apple purchases and restoration', 'Premium purchases use Apple StoreKit. Apple handles payment and account information; the developer does not receive card numbers or payment passwords. The app retrieves prices and verified purchase entitlements to enable ad removal. Apple policies govern purchases, refunds, restoration and Apple retention.'),
   ('Updates and review requests', 'The app queries Apple public lookup services or public TestFlight release information hosted on GitHub to check for updates. Queries may include the app identifier and country; providers may process connection information such as IP addresses. No ledger, receipt or separately generated user identifier is attached to these requests. First-use dates, review request dates and update prompt history are stored on your device. Apple handles review display and reviews you submit.'),
   ('Support requests and this website', 'If you email support, your email address and the information you send are used to respond. Please omit sensitive ledger and receipt details. Inquiry information is processed for support and necessary recordkeeping; contact us below to request deletion. This website has no added analytics tools, advertising, tracking cookies or contact form. The hosting provider may process access logs, including IP addresses and request information, to deliver and secure the pages.'),
   ('Retention, deletion and your choices', 'Ledger records and photos remain on your device until you delete them or delete the app. Delete any copies in exported backups or other storage separately. Use device security and keep backups safe. You can change camera and photo permissions, adjust available advertising consent choices, and contact us with privacy or deletion requests. Google, Apple, hosting and email providers also apply their own policies and retention rules to information they process.'),
   ('International processing and changes', 'Advertising, payment, hosting and email services may process technical or inquiry information outside your country. If app data practices change, this policy and its update date will be revised.'),
   ('Privacy contact', 'Operator: Deokjoo Moon. Support and privacy inquiries: it@bebriz.com.')],
  'providers':'Service provider policies', 'footer':'Your ledger on your device. Help within reach.'
 }
}

CSS = '''*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:#f8f7f2;color:#203d35;font:16px/1.85 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}a{color:#176a50;text-underline-offset:4px}a:hover{color:#0a4332}a:focus-visible,summary:focus-visible{outline:3px solid #dc9448;outline-offset:5px}header,main,footer{max-width:1000px;margin:auto;padding:24px}header{display:flex;align-items:center;justify-content:space-between;gap:16px;border-bottom:1px solid #dfe5dd}.brand{font-size:21px;font-weight:750;text-decoration:none;display:flex;align-items:center;gap:12px}.brand img{width:42px;height:42px;border-radius:12px}nav{display:flex;flex-wrap:wrap;gap:20px;align-items:center;font-size:14px}.languages{display:flex;gap:10px}main{padding-top:56px;padding-bottom:72px}.eyebrow{font-size:13px;letter-spacing:2px;color:#64776a}h1{font-size:clamp(32px,6vw,54px);line-height:1.3;letter-spacing:-1.5px;margin:16px 0 24px}h2{font-size:23px;line-height:1.5;margin:36px 0 12px}p{margin:0 0 20px}.lead{max-width:660px;font-size:19px;color:#56695f}.contact{margin:38px 0 52px;padding:28px;background:#e8efe5;border-radius:18px;max-width:740px}.contact h2{margin:0 0 12px}.button{display:inline-block;padding:11px 20px;border-radius:10px;background:#235c47;color:white;text-decoration:none;font-weight:650}.button:hover{background:#184735;color:white}.email{display:block;margin:12px 0}.document{max-width:740px}.document h2{padding-top:12px;border-top:1px solid #dfe5dd}.date{color:#67776b;font-size:14px}details{border-bottom:1px solid #dfe5dd;padding:18px 0}summary{cursor:pointer;font-weight:650}details p{margin:14px 0 0;color:#53665b}footer{border-top:1px solid #dfe5dd;font-size:13px;color:#66776b;display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap}.skip{position:absolute;left:-9999px}.skip:focus{left:12px;top:12px;background:white;padding:8px;z-index:5}@media(max-width:600px){header{align-items:flex-start;flex-direction:column;padding:18px 22px}nav{gap:16px}main{padding:30px 22px 48px}.contact{padding:22px}h1{letter-spacing:-.7px}body{overflow-wrap:anywhere}}@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}'''
PROVIDERS = [
 ('Google Privacy Policy', 'https://policies.google.com/privacy'),
 ('Google Mobile Ads SDK data disclosure', 'https://developers.google.com/admob/ios/privacy/data-disclosure'),
 ('Apple Privacy Policy', 'https://www.apple.com/legal/privacy/'),
 ('GitHub Privacy Statement', 'https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement'),
]

def page(lang, kind):
 c=CONTENT[lang]
 is_privacy=kind=='privacy'
 title=c['privacy'] if is_privacy else c['support']
 nav=''.join(f'<a href="/{code}/{kind}/" lang="{code}"{ " aria-current=\"page\"" if code==lang else ""}>{name}</a>' for code,name in [('ko','한국어'),('en','English')])
 if is_privacy:
  body=f'<p class="date">{c["effective"]}</p><p class="lead">{c["policyIntro"]}</p>'
  for heading,paragraph in c['sections']:
   body+=f'<section><h2>{escape(heading)}</h2><p>{escape(paragraph)}</p></section>'
  body+=f'<h2>{c["providers"]}</h2><ul>'+''.join(f'<li><a href="{url}">{name}</a></li>' for name,url in PROVIDERS)+'</ul>'
  body+=f'<a class="button" href="mailto:{EMAIL}">{c["mail"]}</a>'
 else:
  body=f'<p class="lead">{c["intro"]}</p><section class="contact"><h2>{c["contact"]}</h2><p>{c["contactText"]}</p><a class="button" href="mailto:{EMAIL}">{c["mail"]}</a><a class="email" href="mailto:{EMAIL}">{EMAIL}</a></section><section class="document"><h2>{c["faq"]}</h2>'
  body+=''.join(f'<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>' for q,a in c['questions'])+'</section>'
 document = f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="{escape(c['policyIntro'] if is_privacy else c['intro'],quote=True)}"><meta name="color-scheme" content="light"><title>{c['brand']} · {title}</title><link rel="icon" href="/icon.png"><link rel="stylesheet" href="/style.css"></head><body><a class="skip" href="#main">Skip to content</a><header><a class="brand" href="/{lang}/support/"><img src="/icon.png" alt="" width="42" height="42">{c['brand']}</a><nav aria-label="Navigation"><a href="/{lang}/support/">{c['support']}</a><a href="/{lang}/privacy/">{c['privacy']}</a><span class="languages">{nav}</span></nav></header><main id="main"><div class="eyebrow">MONEYWAVES</div><h1>{title if is_privacy else c['tag']}</h1><article class="document">{body}</article></main><footer><span>{c['footer']}</span><span>© 2026 {OWNER} · <a href="mailto:{EMAIL}">{EMAIL}</a></span></footer></body></html>'''
 return document.replace('href="/', f'href="{BASE}/').replace('src="/', f'src="{BASE}/')

OUT.mkdir(exist_ok=True)
(OUT/'style.css').write_text(CSS)
for lang in CONTENT:
 for kind in ['support','privacy']:
  target=OUT/lang/kind
  target.mkdir(parents=True,exist_ok=True)
  (target/'index.html').write_text(page(lang,kind))
(OUT/'index.html').write_text(page('ko','support'))
(OUT/'app-ads.txt').write_text('google.com, pub-3315039775230573, DIRECT, f08c47fec0942fa0\n')
(OUT/'robots.txt').write_text('User-agent: *\nAllow: /\n')
(OUT/'.nojekyll').write_text('')
import shutil
shutil.copyfile(ROOT/'assets/icon.png', OUT/'icon.png')
print('Built support and privacy pages in Korean and English.')
