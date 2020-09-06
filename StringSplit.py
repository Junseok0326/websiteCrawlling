import requests
from bs4 import BeautifulSoup
import re

req = requests.get("http://www.saramin.co.kr/zf_user/educe/spec-information/index/page/1?page=1&page_count=10&type=major&major_sub=maj031&major=maj073&listType=spec")
html = req.text
soup = BeautifulSoup(html, "html.parser")

row = soup.select(
"#content > div.wrap_pass_spec > div.list_spec_result > div.company_list.spec_grid > div > div.spec_detail > div.left_info > table > tbody > tr:nth-child(2) > td:nth-child(2) > dl > dd"
)
for item in row:
    text = item.text
    regex = re.compile("\d")
    match = regex.search(text)
    print(match.group(0))
    print(item.text)