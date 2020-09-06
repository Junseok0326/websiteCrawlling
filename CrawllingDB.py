
import requests
import csv
from bs4 import BeautifulSoup

#사람인 데이터 받아오기
def dataParsing(url,arr):
    dataItem = soup.select(url)
    virArr = []
    for data in dataItem:
        virArr.append(data.text)
    arr.append(virArr)

#대학별로 값 분배하기
def uniVal(arr1, arr2):
    for j in range(len(rowLen)):
        csvInsetArr = []
        for i in range(urlLen):
            csvInsetArr.append(arr1[i][j])
        arr2.append(csvInsetArr)

#csv쓰기
def writeCsv(arr,f):
    csv_writer = csv.writer(f)
    csv_writer.writerow(first_colum)
    for index in arr:
        csv_writer.writerow(index)

fileName = 'saraminResult_ComputerMajor.csv'
f = open('%s'%fileName, 'w', newline="")
#csv에 들어갈 첫행 데이터 목록
first_colum = ['대학명','계열','학점','토익','토스','오픽','자격증','수상경험','인턴','해외경험','봉사활동','기업명','부서']

#데이터 추출 함수
uniUrl = []
uniUrl.append("div.wrap_company_info > dl > dd:nth-child(2)")#대학명
uniUrl.append("div.wrap_company_info > dl > dd:nth-child(3)")#계열
for i in range(1,4):
    for j in range(1,4):
        uniUrl.append(
            "div.company_list.spec_grid > div > div.spec_detail > div.left_info > table > tbody > tr:nth-child(%d) > td:nth-child(%d) > dl > dd"%(i,j)
        )
uniUrl.append("div.company_list.spec_grid > div > div.wrap_company_info > h2 > a")# 기업명
uniUrl.append("div.company_list.spec_grid > div > div.wrap_company_info > dl > dt")# 부서


uniArr = []
uniName_arr = []
uniMajor_arr = []
uniItemArr = []
uniCsvArr = []

urlLen = len(uniUrl)
page = 1
rowLen = [1,2,3,4,5,6,7,8,9,10]


while True:
    req = requests.get("http://www.saramin.co.kr/zf_user/educe/spec-information/index/page/%d?page=1&page_count=10&type=major&major_sub=maj028&major=maj057&listType=spec"%page)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    #row클래스 개수 세기
    rowLen = []
    rowLen = soup.select('.row')


    for index in range(urlLen):
        dataParsing(uniUrl[index],uniItemArr)
    uniVal(uniItemArr,uniCsvArr)
    del(uniItemArr)
    uniItemArr=[]
    print("page : %d row개수 : %d" % (page, len(rowLen)))
    page += 1

    if(len(rowLen) != 10):
        break;

writeCsv(uniCsvArr, f)
f.close()