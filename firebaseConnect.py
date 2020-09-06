import requests
from bs4 import BeautifulSoup
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import re

# Use a service account
cred = credentials.Certificate('mobileprojectjs-2019-firebase-adminsdk-0ehsl-5bbc8daac4.json')
firebase_admin.initialize_app(cred)

def strRegex(item,arr):
    text = item.text
    regex = re.compile("\d")
    match = regex.search(text)
    arr.append(int(match.group(0)))

def strSplit(item):
    textArr = item.split('/')
    for i in range(len(textArr)):
        if(i==0):
            text = textArr[0]
        else:
            text+=", %s"%textArr[i]
    return text

def corpSplit(data, arr):
    item = data.text;
    textArr = item.split('/')
    if(len(textArr[0].split(' '))>1):
        text = ''.join(textArr[0].split(' '))
    else:
        text = textArr[0]
    arr.append(text)


def strEqual(data, arr):
    toeic = data.text
    if (toeic == "없음"):
        toeic = 0
    else:
        toeic = int(toeic)
    arr.append(toeic)

#사람인 데이터 받아오기
def dataParsing(url,arr,index):
    dataItem = soup.select(url)
    virArr = []
    for data in dataItem:
        if(index==2):
            virArr.append(float(data.text.split(' ')[0]))
        elif(index==3):
            strEqual(data,virArr)
        elif(index==6):
            strRegex(data,virArr)
        elif (index == 7):
            strRegex(data, virArr)
        elif (index == 8):
            strRegex(data, virArr)
        elif (index == 9):
            strRegex(data, virArr)
        elif (index == 10):
            strRegex(data, virArr)
        elif (index == 11):
            corpSplit(data, virArr)
        else:
            virArr.append(data.text)
    arr.append(virArr)

itemCnt = 0

def changeG():
    global itemCnt

#대학별로 값 분배하기
def uniVal(arr1,itemCnt,page):
    for j in range(len(rowLen)):
        dataInsetArr = []
        for i in range(urlLen):
            dataInsetArr.append(arr1[i][j])
        db = firestore.client()
         #유저_대학명 계열 학점 토익 자격증 수상경험 인턴 해외경험 봉사활동 문서명 설정하기
        # '대학명','계열','학점','토익','토스','오픽','자격증','수상경험','인턴','해외경험','봉사활동','기업명','부서'
        strSplit(dataInsetArr[1])
        # doc_name="%s%d"%(dataInsetArr[0],strSplit(dataInsetArr[1]),dataInsetArr[2],dataInsetArr[3],dataInsetArr[6],dataInsetArr[7],dataInsetArr[8],dataInsetArr[9],dataInsetArr[10],itemCnt)

        doc_name = 'user%d_%d'%(page-1,j)
        itemCnt=itemCnt+1

        doc_ref = db.collection(u'specData').document(str(doc_name))
        #doc_ref = db.collection(u'corpData').document(str(doc_name))
        #for i in range(len(arr)):

        doc_ref.set({
                u'college': u'%s'%dataInsetArr[0],
                u'major': u'%s'%dataInsetArr[1],
                u'grade': dataInsetArr[2],
                u'toeic': dataInsetArr[3],
                u'toeicSpeaking': u'%s'%dataInsetArr[4],
                u'opic': u'%s'%dataInsetArr[5],
                u'license': dataInsetArr[6],
                u'award': dataInsetArr[7],
                u'intern': dataInsetArr[8],
                u'overseas': dataInsetArr[9],
                u'volun': dataInsetArr[10],
                u'corporation': u'%s'%dataInsetArr[11],
                u'department': u'%s'%dataInsetArr[12]
            #u'department':[dataInsetArr[12]]
        })




#db에 들어갈 첫행 데이터 목록
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

urlLen = len(uniUrl)
page = 2013
rowLen = [1,2,3,4,5,6,7,8,9,10]


while len(rowLen) == 10:
    print("page : %d row개수 : %d"%(page,len(rowLen)))
    req = requests.get("http://www.saramin.co.kr/zf_user/educe/spec-information/index/page/%d?page=1&page_count=10&type=major&listType=spec"%page)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    #row클래스 개수 세기
    rowLen = []
    rowLen = soup.select('.row')

    for index in range(urlLen):
        dataParsing(uniUrl[index],uniItemArr,index)
    uniVal(uniItemArr,itemCnt,page)
    del(uniItemArr)
    uniItemArr=[]
    page += 1
