# -*- coding: utf-8 -*-
from flask import Flask, request
import pymysql as sql
import requests as req

app = Flask(__name__)
'''
{'post_type': 'message', 'message_type': 'group', 'time': 1683945825, 'self_id': 1978436936, 'sub_type': 'normal', 'sender': {'age': 0, 'area': '', 'card': '', 'level': '', 'nickname': '小井井', 'role': 'member', 'sex': 'unknown', 'title': '', 'user_id': 771732203}, 'message_id': 724760386, 'message_seq': 63318, 'raw_message': '1231312312312312312312312312', 'user_id': 771732203, 'anonymous': None, 'font': 0, 'group_id': 139631967, 'message': '1231312312312312312312312312'}
1231312312312312312312312312
['1231312312312312312312312312']
'''
'''{'post_type': 'message', 'message_type': 'private', 'time': 1684236504, 'self_id': 1978436936, 'sub_type': 'friend', 'me
ssage_id': -866267682, 'user_id': 771732203, 'target_id': 1978436936, 'message': '123123', 'raw_message': '123123', 'fon
t': 0, 'sender': {'age': 0, 'nickname': '小井井', 'sex': 'unknown', 'user_id': 771732203}}'''
'''
{'post_type': 'notice', 'notice_type': 'group_recall', 'time': 1683945825, 'self_id': 1978436936, 'group_id': 139631967, 'user_id': 771732203, 'operator_id': 771732203, 'message_id': 724760386}'''
'''{'post_type': 'notice', 'notice_type': 'friend_recall', 'time': 1684236068, 'self_id': 1978436936, 'user_id': 771732203,
 'message_id': -1632885063}'''
mysql = sql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='python_mysql_data',
                    charset='utf8mb4')
curser = mysql.cursor()


@app.route("/", methods=["post"])
def get_json():
    request_get_json = request.get_json()
    try:
        if request_get_json['post_type'] != 'meta_event':
            print(request_get_json)
            if request_get_json['post_type'] == 'notice':
                if request_get_json['notice_type'] == 'group_recall':
                    message_id = request_get_json['message_id']
                    command = '''SELECT * FROM GROUP_MESSAGE WHERE MESSAGE_ID = '{}';'''.format(message_id)
                    curser.execute(command)
                    data = curser.fetchone()
                    print(data)
                    if data[-4]:
                        req.get('http://127.0.0.1:5700/send_group_msg?group_id={}&message={}'.format(data[-2], '有人撤回了！数据库id编号：{}，发送时间（时间戳）：{}，发送人QQ号：{}，发送人昵称：{}，发送人级别：{}，消息id：{}，消息（真消息+假消息）{}；{}，群号：{}，匿名发送？{}。'.format(data[0], data[1], data[3], data[4], data[9], data[-7], data[-5], data[-1], data[-2], 'False')))
                    else:
                        req.get('http://127.0.0.1:5700/send_group_msg?group_id={}&message={}'.format(data[-2], '有人撤回了！数据库id编号：{}，发送时间（时间戳）：{}，发送人QQ号：{}，发送人昵称：{}，发送人级别：{}，消息id：{}，消息（真消息+假消息）{}；{}，群号：{}，匿名发送？{}。'.format(data[0], data[1], data[3], data[4], data[9], data[-7], data[-5], data[-1], data[-2], 'True')))
                if request_get_json['notice_type'] == 'friend_recall':
                    message_id = request_get_json['message_id']
                    command = '''SELECT * FROM PRIVATE_MESSAGE WHERE MESSAGE_ID = '{}';'''.format(message_id)
                    curser.execute(command)
                    data = curser.fetchone()
                    print(data)
                    req.get('http://127.0.0.1:5700/send_private_msg?user_id={}&message={}'.format(data[-2],
                                                                                                     '数据库id编号：{}，发送时间：{}，消息ID：{}，用户ID：{}，消息（真消息，消息）：{}：{}，发送人：{}。'.format(data[0], data[1], data[3], data[4], data[-5], data[-6], data[-2])))
            elif request_get_json['post_type'] == 'message':
                if request_get_json['message_type'] == 'group':
                    time = request_get_json['time']
                    sub_type = request_get_json['sub_type']
                    sender_qq_number = request_get_json['user_id']
                    sender_nickname = request_get_json['sender']['nickname']
                    sender_age = request_get_json['sender']['age']
                    sender_area = request_get_json['sender']['area']
                    sender_card = request_get_json['sender']['card']
                    sender_level = request_get_json['sender']['level']
                    sender_role = request_get_json['sender']['role']
                    sender_sex = request_get_json['sender']['sex']
                    sender_message_title = request_get_json['sender']['title']
                    message_id = request_get_json['message_id']
                    message_seq = request_get_json['message_seq']
                    raw_message = request_get_json['raw_message']
                    anonymous = request_get_json['anonymous']
                    font = request_get_json['font']
                    group_id = request_get_json['group_id']
                    message = request_get_json['message']
                    id = curser.execute('''SELECT ID FROM GROUP_MESSAGE''') + 1
                    command = '''INSERT INTO GROUP_MESSAGE (ID, TIME, SUB_TYPE, SENDER_QQ_NUMBER, SENDER_NICKNAME, 
                    SENDER_AGE, SENDER_AREA, SENDER_CARD, SENDER_LEVEL, SENDER_ROLE, SENDER_SEX, 
                    SENDER_MESSAGE_TITLE, MESSAGE_ID, MESSAGE_SEQ, RAW_MESSAGE, anoymous, FONT, GROUP_ID, 
                    MESSAGE) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', 
                    '%s', '%s', '%s', '%s', '%s', '%s');'''
                    data = (id, time, sub_type, sender_qq_number, sender_nickname, sender_age, sender_area, sender_card, sender_level, sender_role, sender_sex, sender_message_title, message_id, message_seq, raw_message, anonymous, font, group_id, message)
                    curser.execute(command % data)
                    mysql.commit()
                elif request_get_json['message_type'] == 'private':
                    time = request_get_json['time']
                    sub_type = request_get_json['sub_type']
                    message_id = request_get_json['message_id']
                    user_id = request_get_json['user_id']
                    target_id = request_get_json['target_id']
                    message = request_get_json['message']
                    raw_message = request_get_json['raw_message']
                    font = request_get_json['font']
                    age = request_get_json['sender']['age']
                    nickname = request_get_json['sender']['nickname']
                    sex = request_get_json['sender']['sex']
                    id = curser.execute('''SELECT ID FROM PRIVATE_MESSAGE''') + 1
                    command = '''INSERT INTO PRIVATE_MESSAGE (ID, TIME, SUB_TYPE, MESSAGE_ID, USER_ID, 
                    TARGET_ID, MESSAGE, RAW_MESSAGE, FONT, AGE, NICKNAME, 
                    SEX) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');'''
                    data = (id, time, sub_type, message_id, user_id, target_id, message, raw_message, font, age, nickname, sex)
                    curser.execute(command % data)
                    mysql.commit()
        else:
            pass
    except Exception as e:
        raise
    return "root"


if __name__ == '__main__':
    app.run("0.0.0.0", port=8899)
