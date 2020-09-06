import requests
from bs4 import BeautifulSoup

req = requests.get("http://www.saramin.co.kr/zf_user/educe/spec-information/index/page/1?page=1&page_count=10&type=major&listType=spec")
html = req.text
soup = BeautifulSoup(html, "html.parser")

row = soup.select(
"#content > div.wrap_pass_spec > div.list_spec_result > div.company_list.spec_grid > div > div.spec_detail > div.left_info > table > tbody > tr:nth-child(1) > td:nth-child(2) > dl > dd"
)
arr = []
for item in row:
    toeic = item.text
    if(toeic == "없음"):
        toeic=0
    else:
        toeic = int(item.text)
    arr.append(toeic)
print(arr)