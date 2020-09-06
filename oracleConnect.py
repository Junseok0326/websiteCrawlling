import cx_Oracle

con = cx_Oracle.connect('tony0326/wnstjr7570@localhost:1521/xe')
cur = con.cursor()
list = []
for i in range(10):
    list.append(i)

for item in list:
    cur.execute("insert into tony0326.CONNECTTEST(NAME) values('%s')"%item)
con.commit()

result = cur.execute('select * from tony0326.CONNECTTEST')

for item in result:
    print(item)
    print(type(item))

cur.close()
con.close()
