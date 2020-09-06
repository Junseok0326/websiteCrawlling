import csv
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import re
from collections import OrderedDict

def strSplit(item):
    textArr = item.split('/')
    if(len(textArr[0].split(' '))>1):
        text = ''.join(textArr[0].split(' '))
    else:
        text = textArr[0]
    return text


with open('test.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))
arr = ["모든부서"]
token = 0

# Use a service account
cred = credentials.Certificate('mobileprojectjs-2019-firebase-adminsdk-0ehsl-5bbc8daac4.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
print(len(data))
for i in range(1,len(data)-1):
    arr.append(data[i][1])
    if(data[i+1][0]!=data[i][0]):
        print(strSplit(data[i][0]))

        # print(arr)
        arr = list(OrderedDict.fromkeys(arr))
        print(arr)
        doc_ref = db.collection('corpData').document(strSplit(data[i][0]))
        doc_ref.set({
            u'department': arr
        })
        arr = ["모든부서"]



