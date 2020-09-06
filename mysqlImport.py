import requests
import pymysql
from bs4 import BeautifulSoup

conn = pymysql.connect(host='localhost',
                     user='root',
                     passwd='tiger',
                     db='public_project',
                     charset='utf8')

# try:
#     with conn.cursor() as cursor:
#         sql2 = """
#                     create table passInfo(
#                     pass_gno int(5) not null,
#                     pass_num int(5) not null auto_increment primary key,
#                     pass_year int(4) not null,
#                     pass_company varchar(20) not null,
#                     pass_dept varchar(100),
#                     pass_question varchar(600) not null,
#                     pass_answer varchar(3000));
#                 """
#         cursor.execute(sql2)
#     conn.commit()
# finally:
#     print()

gno = 0

for i in range(2):
    link = 'http://www.saramin.co.kr/zf_user/public-recruit/coverletter-list/page/' + str(i) +'?company_nm=농협'  # 페이지 이동, 기업별로 comapny_nm 다음 바꿔주기(링크 참조)
    req = requests.get(link)
    html = req.content
    soup = BeautifulSoup(html, 'html.parser')

    a = soup.findAll(name='td', attrs={"class": "td_apply_subject"})
    cnt = 0

    for row in a:
        b = row.find('a')['href']          #   http://www.saramin.co.kr 얘추가하기
        req = requests.get('http://www.saramin.co.kr'+b)
        html = req.content
        soup = BeautifulSoup(html, 'html.parser')

        Q = soup.findAll(name='div', attrs={"class": "box_ty3"})
        depart = soup.select('span')
        Y = soup.findAll(name='span', attrs={"class": "txt_recruit"})
        C = soup.findAll("span", {"class":"tit_company_name"})

        if('http://www.saramin.co.kr/zf_user/public-recruit/coverletter?real_seq=30682' != 'http://www.saramin.co.kr'+b) :
            gno += 1
            for row in depart:
                row2 = row.findAll('b')
                for i in row2:
                    length = len(i.text)
                    department = row.text[length + 3:] #분야

            for row in Y :
                year = int(row.text[:4]) #년도
                print(year)
            for row in Q:
                row2 = row.findAll('h3')
                for i in row2:
                    company = C[0].text     # 기업, 기업별로 기업이름 바꿔주기
                    question = i.text # 질문
                    length = len(i.text)
                    answer = row.text[length + 1:-30].strip()  # 답변

                    try:
                        with conn.cursor() as cursor:
                            sql3 = "insert into passInfo( pass_gno, pass_year, pass_company, pass_dept, pass_question, pass_answer) values (%s, %s, %s, %s, %s, %s)"
                            cursor.execute(sql3, (gno, year, company, department, question, answer))
                        conn.commit()
                    finally:
                        print()

conn.close()