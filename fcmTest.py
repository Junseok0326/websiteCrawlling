# -*- coding: utf-8 -*-
import json
import requests

#
# def main(server_key, token, message_body):
#     headers = {
#         'Authorization': 'key= ' + server_key,
#         'Content-Type': 'application/json',
#     }
#
#     data = {
#         'to': token,
#         'data': {
#             'message_body': message_body,
#         },
#     }
#
#     response = requests.post('https://fcm.googleapis.com/fcm/send', headers=headers, data=json.dumps(data))
#     print(response)
#
#
# if __name__ == '__main__':
#     server_key = "AAAAVFTZnik:APA91bGadOo-pamyUCEKftawzJuhsMWQtZ7u-Aq19GKgvM3FPZcz-xTfj80L91Wdzo8TuSCeBEOFgyfAyZnoLudydBdD_njwlXKsdIUFVrZsYuE6NVPO2KxLk_U7hCG0Dp4dJtu2_G7q"  # Firebase Project Settings > CLOUD MESSAGING
#     token = "fiFDMAaL_ZE:APA91bFJi3LAdZg8DpDQdAt9iQDGRphMVZfCvWnEuk-TRFHssRe52RozV8pNeObj9uAP0f6jNt_kOwzucb3PSkUVolA_frOJVYq5aB22GZiP3ZCBQclGrjWaouBNQVVAsg5IeTmMrJ2u"       # User's refreshed Token
#     message_body = '파이썬테스트입미당'    # 푸쉬 메세지
#     main(server_key, token, message_body)