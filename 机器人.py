# -*- coding: utf-8 -*-
from flask import Flask, request
import requests as req
from subprocess import *
from random import *
from json import *
from qrcode import *
from urllib import parse
import openai
from time import *
from binascii import *
import requests
import os
from Crypto.Cipher import AES
import base64
import json
import xlrd

app = Flask(__name__)
cmd_res = {}
item = ''
skip = {}
choose = {}
long = {}
pin = ''
OPonly = False
group_message_id_list = []
private_message_id_list = []
task = []
autosave = False
with open(file='black_list.txt', mode='r+', encoding='utf-8') as f:
    try:
        blacklist = list(f.readlines())
        blacklist = blacklist[0][1:-1].split(',')
        for temp in range(len(blacklist)):
            blacklist[temp] = int(blacklist[temp])
    except (IndexError, ValueError):
        blacklist = []
    finally:
        f.close()
with open(file='admin_list.txt', mode='r+', encoding='utf-8') as f:
    try:
        adminlist = list(f.readlines())
        adminlist = adminlist[0][1:-1].split(',')
        for temp in range(len(adminlist)):
            adminlist[temp] = int(adminlist[temp])
    except (IndexError, ValueError):
        adminlist = []
    finally:
        f.close()
with open(file='can_use_python_list.txt', mode='r+', encoding='utf-8') as f:
    try:
        python_list = list(f.readlines())
        python_list = python_list[0][1:-1].split(',')
        for temp in range(len(python_list)):
            python_list[temp] = int(python_list[temp])
    except (IndexError, ValueError):
        python_list = []
    finally:
        f.close()
with open(file='chat_gpt_list.txt', mode='r+', encoding='utf-8') as f:
    try:
        chat_gpt_list = list(f.readlines())
        chat_gpt_list = chat_gpt_list[0][1:-1].split(',')
        for temp in range(len(chat_gpt_list)):
            chat_gpt_list[temp] = int(chat_gpt_list[temp])
    except (IndexError, ValueError):
        chat_gpt_list = []
    finally:
        f.close()
with open(file='summon_images_list.txt', mode='r+', encoding='utf-8') as f:
    try:
        summon_images_list = list(f.readlines())
        summon_images_list = summon_images_list[0][1:-1].split(',')
        for temp in range(len(summon_images_list)):
            summon_images_list[temp] = int(summon_images_list[temp])
    except (IndexError, ValueError):
        summon_images_list = []
    finally:
        f.close()
with open(file='group_admin_list.txt', mode='r+', encoding='utf-8') as f:
    try:
        group_admin_list = list(f.readlines())
        group_admin_list = group_admin_list[0][1:-1].split(',')
        for temp in range(len(group_admin_list)):
            group_admin_list[temp] = int(group_admin_list[temp])
    except (IndexError, ValueError):
        group_admin_list = []
    finally:
        f.close()
with open(file='can_use_java_list.txt', mode='r+', encoding='utf-8') as f:
    try:
        java_list = list(f.readlines())
        java_list = java_list[0][1:-1].split(',')
        for temp in range(len(java_list)):
            java_list[temp] = int(java_list[temp])
    except (IndexError, ValueError):
        java_list = []
    finally:
        f.close()
with open(file='can_use_c_list.txt', mode='r+', encoding='utf-8') as f:
    try:
        c_list = list(f.readlines())
        c_list = c_list[0][1:-1].split(',')
        for temp in range(len(c_list)):
            c_list[temp] = int(c_list[temp])
    except (IndexError, ValueError):
        c_list = []
    finally:
        f.close()
with open(file='can_use_python_list.txt', mode='r+', encoding='utf-8') as f:
    try:
        python_list = list(f.readlines())
        python_list = python_list[0][1:-1].split(',')
        for temp in range(len(python_list)):
            python_list[temp] = int(python_list[temp])
    except (IndexError, ValueError):
        python_list = []
    finally:
        f.close()


openai.api_key = ''#填入你的api key


def send_group_message(group, message):
    global group_message_id_list
    message = req.get('http://127.0.0.1:5700/send_group_msg?group_id={}&message={}'.format(group, message))
    group_message_id_list.append(eval(message.content.decode())['data']['message_id'])
    print(group_message_id_list)


def send_private_message(user_id, message):
    global private_message_id_list
    message = req.get('http://127.0.0.1:5700/send_private_msg?user_id={}&message={}'.format(user_id, message))
    private_message_id_list.append(eval(message.content.decode())['data']['message_id'])
    print(private_message_id_list)

def delete_group_message():
    global group_message_id_list
    req.get('http://127.0.0.1:5700/delete_msg?message_id={}'.format(group_message_id_list[len(group_message_id_list) - 1]))
    del group_message_id_list[len(group_message_id_list) - 1]

def delete_private_message():
    global private_message_id_list
    req.get('http://127.0.0.1:5700/delete_msg?message_id={}'.format(private_message_id_list[len(private_message_id_list) - 1]))
    del private_message_id_list[len(private_message_id_list) - 1]


CODE = {'A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.',
        '%': '-..-.-'
        }


class Mosi(object):
    def __init__(self, code: dict):
        self.code = code

    def encode(self, string: str):
        pass

    def decode(self, string: int):
        pass


class Encode(Mosi):
    def __init__(self, code: dict):
        super().__init__(code)
        self.string = ''
        self.string_list = []
        self.mosi = []
        self.new_string = ''
        self.print_string = ''

    def encode(self, string: str):
        self.string = string.upper()
        for temp in self.string:
            self.string_list.append(temp)
        for temp1 in self.string_list:
            self.mosi.append(self.code[temp1])
        for temp2 in range(len(self.mosi)):
            self.new_string += self.mosi[temp2]
            self.new_string += '|'
        for temp3 in self.new_string:
            if temp3 == '.':
                self.print_string += 'A'
            elif temp3 == '-':
                self.print_string += 'B'
            elif temp3 == '|':
                self.print_string += 'C'
        self.print_string = int(self.print_string, 16)
        return self.print_string / 99999999999999999999


class Decode(Mosi):
    def __init__(self, code: dict):
        super().__init__(code)
        self.int_string = 0
        self.new_string = ''
        self.mosi_list = []
        self.code_keys = []
        self.print_string = ''

    def decode(self, int_string: float):
        self.int_string = int_string * 99999999999999999999
        self.int_string = hex(int(self.int_string))
        self.int_string = str(self.int_string).upper()
        for temp in self.int_string:
            if temp == 'A':
                self.new_string += '.'
            elif temp == 'B':
                self.new_string += '-'
            elif temp == 'C':
                self.new_string += '|'
        temp2 = ''
        for temp1 in self.new_string:
            if temp1 == '|':
                self.mosi_list.append(temp2)
                temp2 = ''
            else:
                temp2 += temp1
        for temp3 in range(len(self.mosi_list)):
            for temp4, temp5 in self.code.items():
                if self.mosi_list[temp3] == self.code[temp4]:
                    self.print_string += temp4
                    continue
        self.print_string = self.print_string.lower()
        return self.print_string


class SongSearchFail(object):
    pass


class Encrypyed():
    '''加密生成'params'、'encSecKey 返回'''

    def __init__(self):
        self.pub_key = '010001'
        self.modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
        self.nonce = '0CoJUm6Qyw8W8jud'

    def create_secret_key(self, size):
        return hexlify(os.urandom(size))[:16].decode('utf-8')

    def aes_encrypt(self, text, key):
        iv = '0102030405060708'
        pad = 16 - len(text) % 16
        text = text + pad * chr(pad)
        key = key.encode('utf-8')
        iv = iv.encode('utf-8')
        encryptor = AES.new(key, AES.MODE_CBC, iv)
        text = text.encode('utf-8')
        result = encryptor.encrypt(text)
        result_str = base64.b64encode(result).decode('utf-8')
        return result_str

    def rsa_encrpt(self, text, pubKey, modulus):
        text = text[::-1]
        rs = pow(int(hexlify(text.encode('utf-8')), 16), int(pubKey, 16), int(modulus, 16))
        return format(rs, 'x').zfill(256)

    def work(self, ids, br=128000):
        text = {'ids': [ids], 'br': br, 'csrf_token': ''}
        text = json.dumps(text)
        i = self.create_secret_key(16)
        encText = self.aes_encrypt(text, self.nonce)
        encText = self.aes_encrypt(encText, i)
        encSecKey = self.rsa_encrpt(i, self.pub_key, self.modulus)
        data = {'params': encText, 'encSecKey': encSecKey}
        return data

    def search(self, text):
        text = json.dumps(text)
        i = self.create_secret_key(16)
        encText = self.aes_encrypt(text, self.nonce)
        encText = self.aes_encrypt(encText, i)
        encSecKey = self.rsa_encrpt(i, self.pub_key, self.modulus)
        data = {'params': encText, 'encSecKey': encSecKey}
        return data


class search():
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/55.0.2883.87 Safari/537.36',
            'Host': 'music.163.com',
            'Referer': 'http://music.163.com/search/'}
        self.main_url = 'http://music.163.com/'
        self.session = requests.Session()
        self.session.headers = self.headers
        self.ep = Encrypyed()

    def search_song(self, search_content, search_type=1, limit=9):
        url = 'http://music.163.com/weapi/cloudsearch/get/web?csrf_token='
        text = {'s': search_content, 'type': search_type, 'offset': 0, 'sub': 'false', 'limit': limit}
        data = self.ep.search(text)
        resp = self.session.post(url, data=data)
        result = resp.json()
        if result['result']['songCount'] <= 0:
            return SongSearchFail()
        else:
            songs = result['result']['songs']
            retsult = []
            for song in songs:
                song_id, song_name, singer, alia = song['id'], song['name'], song['ar'][0]['name'], song['al']['name']
                retsult.append([song['id'], song['name'], song['ar'][0]['name'], song['al']['name']])
            return retsult


def diange(name_song, n=0):
    songsearch = search()
    if "宽宽" in name_song:
        return "别欺负宽宽"
    retsult = songsearch.search_song(name_song)
    if type(retsult) == SongSearchFail:
        return "对不起哦没找到名为《" + name_song + "》的歌"
    if len(retsult) > 10:
        retsult = retsult[:10]
    print(retsult)
    if n != None:
        try:
            n = int(n)
        except Exception as err:
            return "n值不合法:" + n
        if n > len(retsult):
            return "n值超过范围"
        else:
            retsult = "[CQ:music,type=163,id=" + str(retsult[n][0]) + "]"
            return retsult
    returnValues = ""
    for i in range(len(retsult)):
        returnValues += "---%d---\n歌曲:%s\n歌手:%s\n专辑:%s\n" % (
            i, retsult[i][1], retsult[i][2], retsult[i][3])
    return returnValues

@app.route("/", methods=["post"])
def get_json():
    # for _ in range(3):
        global skip
        global cmd_res
        global blacklist
        global adminlist
        global item
        global choose
        global pin
        global long
        global group_admin_list
        global OPonly
        global chat_gpt_list
        global summon_images_list
        global c_list
        global java_list
        global autosave
        global python_list
        request_get_json = request.get_json()
        # print(request_get_json)
        if type(request_get_json) == '<class dict>':
            pass
        else:
            try:
                if request_get_json['post_type'] != 'meta_event':
                    if request_get_json['post_type'] == 'notice':
                        if request_get_json['notice_type'] == 'group_increase':
                            send_group_message(request['group_id'], '[CQ:at,qq={}] 欢迎！'.format(request_get_json['user_id']))
                        if request_get_json['notice_type'] == 'group_decrease':
                            send_group_message(request['group_id'], '[CQ:at,qq={}] byebye了您嘞！'.format(request_get_json['user_id']))
                    elif request_get_json['post_type'] == 'request':
                        if request_get_json['request_type'] == 'friend':
                            req.get('http://127.0.0.1:5700/set_friend_add_request?flag={}'.format(request_get_json['flag']))
                            send_private_message(request_get_json['user_id'], '已成功加为好友！')
                        if request_get_json['request_type'] == 'group':
                            req.get('http://127.0.0.1:5700/set_group_add_request?flag={}&sub_type={}'.format(request_get_json['flag'], request_get_json['sub_type']))
                            send_private_message(request_get_json['user_id'], '已通过加群申请！')
                    elif request_get_json['message_type'] == 'group':
                        group = request_get_json['group_id']
                        user_id = request_get_json['sender']['user_id']
                        message_ = request_get_json['message']
                        if '&#91;' in message_:
                            message_ = message_.replace('&#91;', '[')
                        if '&#93;' in message_:
                            message_ = message_.replace('&#93;', ']')
                        if '&amp;' in message_:
                            message_ = message_.replace('&amp;', '&')
                        print(message_)
                        message = message_.split(' ', 4)
                        print(message)
                        print('收件类型：{}，接收人：{}，发送人：{}，QQ号：{}，消息：{}，群：{}'.format(request_get_json['message_type'],
                                                                                                             request_get_json
                                                                                                             ['self_id'],
                                                                                                             request_get_json['sender'][
                                                                                                                 'nickname'],
                                                                                                             request_get_json['sender'][
                                                                                                                 'user_id'],
                                                                                                             request_get_json['message'],
                                                                                                             request_get_json['group_id']))
                        try:
                            if message[0] == '[CQ:at,qq=1978436936]' or message[0] == 'ai':
                                if user_id not in blacklist:
                                    print(message)
                                    if not OPonly or user_id in adminlist:
                                        if '你好' == message[1]:
                                            # 你好功能
                                            send_group_message(group,
                                            '[CQ:at,qq={}] 你好呀\n我是@QQ小井井开发的机器人\n功能不太足\n可以用另外一个人的\nQQ号：2439973472\n版本：beta5.0.0\n请多多关照\n[CQ:image,file=网站.png]！'.format(user_id))
                                        elif '功能' == message[1]:
                                            # 功能功能
                                            send_group_message(group, '[CQ:at,qq={}]hello，我是[CQ:at,'
                                                                      'qq=771732203]研发的机器人，\n功能1：你好打招呼功能\n功能2：查询功能功能\n功能3'
                                                                      '：运行python'
                                                                      '功能\n功能4：投票功能\n功能5：抽奖\n功能6：接龙\n功能7：查询天气\n功能8：生成二维码\n功能9'
                                                                      '：撤回消息（无消息）\n功能10：加/解密\n功能11：chatgpt'
                                                                      '问答（作者申请了好久的账号，给点赞助吧！）\n功能12：赞助\n功能13：反馈\n功能14：管理员\n功能15：群聊设置\n功能16：运行Java\n功能17：运行c\n功能18：生成图片\n功能19：功能用法查询'
                                                                      '即将开发：搜索音乐！\n可以联系['
                                                                      'CQ:at,qq=771732203]反馈哟！'.format(user_id))
                                        elif '查询功能' == message[1]:
                                            gn = message[2]
                                            if gn == '运行python':
                                                send_group_message(group, '[CQ:at,qq={}] 用法为：at 运行python （代码）（注：需要权限）'.format(user_id))
                                            elif gn == '运行java':
                                                send_group_message(group, '[CQ:at,qq={}] 用法为：at 运行java （代码）（注：需要权限）'.format(user_id))
                                            elif gn == '运行c':
                                                send_group_message(group, '[CQ:at,qq={}] 用法为：at 运行c （代码）（注：需要权限）'.format(user_id))
                                            elif gn == '投票':
                                                if message[3] == '发起':
                                                    send_group_message(group, '[CQ:at,qq={}] 用法为：at 发起投票 （名字） （选项数） （选项1） （选项2）...（选项n）'.format(user_id))
                                                elif message[3] == '加入':
                                                    send_group_message(group,
                                                                       '[CQ:at,qq={}] 用法为：at 投票给 （名称)'.format(user_id))
                                                elif message[3] == '结束':
                                                    send_group_message(group, '[CQ:at,qq={}] 用法为：at 结束投票 （名称)'.format(user_id))
                                            elif gn == '抽奖':
                                                if message[3] == '发起':
                                                    send_group_message(group, '[CQ:at,qq={}] 用法为：at 发起抽奖 （名字） （奖品）'.format(user_id))
                                                elif message[3] == '加入':
                                                    send_group_message(group, '[CQ:at,qq={}] 用法为：at 加入抽奖 （名字）'.format(user_id))
                                                elif message[3] == '结束':
                                                    send_group_message(group, '[CQ:at,qq={}] 用法为：at 结束抽奖 （名字）'.format(user_id))
                                            elif gn == '接龙':
                                                if message[3] == '发起':
                                                    send_group_message(group, '[CQ:at,qq={}] 用法为：at 发起接龙 （名字）'.format(user_id))
                                                elif message[3] == '加入':
                                                    send_group_message(group, '[CQ:at,qq={}] 用法为：at 加入接龙 （名字）'.format(user_id))
                                                elif message[3] == '结束':
                                                    send_group_message(group, '[CQ:at,qq={}] 用法为：at 结束接龙 （名字）'.format(user_id))
                                            elif gn == '查询天气':
                                                send_group_message(group, '[CQ:at,qq={}] 用法为：at 查询天气 （地名）'.format(user_id))
                                            elif gn == '生成二维码':
                                                send_group_message(group, '[CQ:at,qq={}] 用法为：at 生成二维码 （内容）以下为可选：（大小） （长，推荐20） （宽，推荐4） （重复，填是或者否） （填充颜色） （二维码颜色）'.format(user_id))
                                            elif gn == '撤回消息':
                                                send_group_message(group, '[CQ:at,qq={}] 用法为：at 撤回消息'.format(user_id))
                                            elif gn == '加密':
                                                send_group_message(group, '[CQ:at,qq={}] 用法为：at 加密 （文字）'.format(user_id))
                                            elif gn == '解密':
                                                send_group_message(group,
                                                                   '[CQ:at,qq={}] 用法为：at 解密 （文字）'.format(user_id))
                                            elif gn == 'chatgpt':
                                                send_group_message(group, '[CQ:at,qq={}] 用法为：at chat （文字）'.format(user_id))
                                            elif gn == '赞助':
                                                send_group_message(group, '[CQ:at,qq={}] 用法为：at 赞助 （微信或者qq）'.format(user_id))
                                            elif gn == '生成图片 ':
                                                send_group_message(group, '[CQ:at,qq={}] 用法为：at 生成图片 （文字） 可选内容：（大小：只支持256x256,512x512,1024x1024）'.format(user_id))
                                            elif gn == '反馈':
                                                send_group_message(group, '[CQ:at,qq={}] 用法为：at 反馈 （文字）'.format(user_id))
                                            elif gn == '管理员':
                                                send_group_message(group, '[CQ:at,qq={}] 用此功能为内部用法请联系小井井获取权限！'.format(user_id))
                                            elif gn == '群聊设置':
                                                send_group_message(group, '[CQ:at,qq={}] 用此功能为内部用法请联系小井井获取权限！'.format(user_id))
                                            elif gn == '运行java':
                                                send_group_message(group, '[CQ:at,qq={}] at 运行java （代码）'.format(user_id))
                                            elif gn == '运行c':
                                                send_group_message(group,
                                                                   '[CQ:at,qq={}] at 运行c （代码）'.format(user_id))
                                        elif message[1] == '运行python':
                                            # 运行代码功能
                                            if user_id in python_list:
                                                with open(file=r'.\run_command.py', mode='w+', encoding='utf-8') as f:
                                                    message = message_.split(' ', 2)
                                                    f.write(message[2])
                                                    f.close()
                                                with open(file=r'.\run_command.py', mode='r+', encoding='utf-8') as f:
                                                    r = f.read()
                                                    f.close()
                                                if 'os' in r:
                                                    send_group_message(group,
                                                                       '[CQ:at,qq={}] 您的代码中有敏感词！os'.format(user_id))
                                                elif 'subprocess' in r:
                                                    send_group_message(group,
                                                                       '[CQ:at,qq={}] 您的代码中有敏感词！subprocess'.format(
                                                                           user_id))
                                                elif 'commands' in r:
                                                    send_group_message(group,
                                                                       '[CQ:at,qq={}] 您的代码中有敏感词！commands'.format(
                                                                           user_id))
                                                else:
                                                    string = r''#运行，改为你的路径
                                                    cmd_output = []
                                                    cmd_error = []
                                                    run = Popen(string, stderr=PIPE, stdout=PIPE, close_fds=True, shell=True)
                                                    cmd_res['out'] = run.stdout.readlines()
                                                    cmd_res['error'] = run.stderr.readlines()
                                                    for temp in cmd_res['out']:
                                                        cmd_output.append(temp.decode('gbk'))
                                                    for temp in cmd_res['error']:
                                                        cmd_error.append(temp.decode('gbk'))
                                                    for temp in range(len(cmd_error)):
                                                        cmd_error[temp] = cmd_error[temp].replace('\r\n', '    ')
                                                    for temp in range(len(cmd_output)):
                                                        cmd_output[temp] = cmd_output[temp].replace('\r\n', '    ')
                                                    send_group_message(request_get_json['group_id'],
                                                                       '[CQ:at,qq={}] 运行结果：\n输出：{}，\n错误：{}'.format(
                                                                           user_id, cmd_output, cmd_error))
                                            else:
                                                send_group_message(group, '[CQ:at,qq={}] 您无法使用python！'.format(user_id))
                                        elif message[1] == '运行java':
                                            # 运行代码功能
                                            if user_id in java_list:
                                                with open(file=r'.\Main.java', mode='w+', encoding='utf-8') as f:
                                                    message = message_.split(' ', 2)
                                                    f.write(message[2])
                                                    f.close()
                                                string = r'' #运行，改为你的路径
                                                cmd_output = []
                                                cmd_error = []
                                                run = Popen(string, stderr=PIPE, stdout=PIPE, close_fds=True, shell=True)
                                                cmd_res['out'] = run.stdout.readlines()
                                                cmd_res['error'] = run.stderr.readlines()
                                                for temp in cmd_res['out']:
                                                    cmd_output.append(temp.decode('gbk'))
                                                for temp in cmd_res['error']:
                                                    cmd_error.append(temp.decode('gbk'))
                                                for temp in range(len(cmd_error)):
                                                    cmd_error[temp] = cmd_error[temp].replace('\r\n', '    ')
                                                for temp in range(len(cmd_output)):
                                                    cmd_output[temp] = cmd_output[temp].replace('\r\n', '    ')
                                                send_group_message(group,
                                                                   '[CQ:at,qq={}] 运行结果：\n输出：{}，\n错误：{}'.format(
                                                                       user_id, cmd_output, cmd_error))
                                            else:
                                                send_group_message(group, '[CQ:at,qq={}] 您无法使用java！'.format(user_id))
                                        elif message[1] == '运行c':
                                            # 运行代码功能
                                            if user_id in c_list:
                                                with open(file=r'.\library.c', mode='w+', encoding='utf-8') as f:
                                                    message = message_.split(' ', 2)
                                                    f.write(message[2])
                                                    f.close()
                                                string = r'' #编译器，改为你的路径
                                                cmd_output = []
                                                cmd_error = []
                                                run = Popen(string, stderr=PIPE, stdout=PIPE, close_fds=True, shell=True)
                                                cmd_res['out'] = run.stdout.readlines()
                                                cmd_res['error'] = run.stderr.readlines()
                                                for temp in cmd_res['out']:
                                                    cmd_output.append(temp.decode('gbk'))
                                                for temp in cmd_res['error']:
                                                    cmd_error.append(temp.decode('gbk'))
                                                for temp in range(len(cmd_error)):
                                                    cmd_error[temp] = cmd_error[temp].replace('\r\n', '    ')
                                                for temp in range(len(cmd_output)):
                                                    cmd_output[temp] = cmd_output[temp].replace('\r\n', '    ')
                                                send_group_message(group,
                                                                   '[CQ:at,qq={}] 编译结果：\n输出：{}，\n错误：{}'.format(
                                                                       user_id, cmd_output, cmd_error))
                                                string = r'' #运行，改为你的路径
                                                cmd_output = []
                                                cmd_error = []
                                                run = Popen(string, stderr=PIPE, stdout=PIPE, close_fds=False)
                                                cmd_res['out'] = run.stdout.readlines()
                                                cmd_res['error'] = run.stderr.readlines()
                                                for temp in cmd_res['out']:
                                                    cmd_output.append(temp.decode('gbk'))
                                                for temp in cmd_res['error']:
                                                    cmd_error.append(temp.decode('gbk'))
                                                for temp in range(len(cmd_error)):
                                                    cmd_error[temp] = cmd_error[temp].replace('\r\n', '    ')
                                                for temp in range(len(cmd_output)):
                                                    cmd_output[temp] = cmd_output[temp].replace('\r\n', '    ')
                                                send_group_message(group,
                                                                   '[CQ:at,qq={}] 运行结果：\n输出：{}，\n错误：{}'.format(
                                                                       user_id, cmd_output, cmd_error))
                                            else:
                                                send_group_message(group, '[CQ:at,qq={}] 您无法使用c！'.format(user_id))
                                        elif '投票' in message[1]:
                                            if '发起' in message[1]:
                                                item = message_.split(' ', int(message[3]) + 3)
                                                send_group_message(group, '[CQ:at,qq={}] 发起投票成功！'.format(user_id))
                                                print(item)
                                                skip[item[2]] = {}
                                                print(skip)
                                                for temp in range(0, len(item) - 4):
                                                    skip[item[2]][item[temp + 4]] = 0
                                                    print(skip)
                                            elif '给' in message[1]:
                                                name = message[2]
                                                xuanxiang = message[3]
                                                if name not in skip:
                                                    send_group_message(group, '[CQ:at,qq={}] 没有这个投票名称！'.format(user_id))
                                                elif xuanxiang not in skip[name]:
                                                    send_group_message(group, '[CQ:at,qq={}] 没有这个投票选项！'.format(user_id))
                                                else:
                                                    skip[name][xuanxiang] += 1
                                                    send_group_message(group, '[CQ:at,qq={}] 投票成功！'.format(user_id))
                                                    print(skip[name])
                                            elif '结束' in message[1]:
                                                name = message[2]
                                                if name not in skip:
                                                    send_group_message(group,
                                                                       '[CQ:at,qq={}] 没有说这个投票名称！'.format(user_id))
                                                else:
                                                    send_group_message(group,
                                                                       '[CQ:at,qq={}] 投票结束！名字：{}，{}'.format(user_id, name,
                                                                                                                  skip[name]))
                                                    del skip[name]
                                        elif '抽奖' in message[1]:
                                            if '发起' in message[1]:
                                                name = message[2]
                                                pin = message[3]
                                                choose[name] = []
                                                send_group_message(group, '[CQ:at,qq={}] 开始抽奖！'.format(user_id))
                                                print(choose)
                                            elif '加入' in message[1]:
                                                name = message[2]
                                                if name not in choose:
                                                    send_group_message(group, '[CQ:at,qq={}] 没有这个抽奖！'.format(user_id))
                                                else:
                                                    choose[name].append(request_get_json['sender']['nickname'])
                                                    send_group_message(group, '[CQ:at,qq={}] 加入成功，昵称：{}'.format(user_id,
                                                                                                                      request_get_json[
                                                                                                                          'sender'][
                                                                                                                          'nickname']))
                                                    print(choose)
                                            elif '结束' in message[1]:
                                                name = message[2]
                                                if name not in choose:
                                                    send_group_message(group, '[CQ:at,qq={}] 没有这个抽奖！'.format(user_id))
                                                else:
                                                    jiang = choice(choose[name])
                                                    send_group_message(group,
                                                                       '@{} 你中了奖！本次参与抽奖的人有{}，奖品是：{}'.format(
                                                                           jiang,
                                                                           choose[
                                                                               name],
                                                                           pin))
                                                    print(choose)
                                                    del choose[name]
                                        elif '接龙' in message[1]:
                                            if '发起' in message[1]:
                                                name = message[2]
                                                long[name] = []
                                                send_group_message(group, '[CQ:at,qq={}] 创建接龙成功！'.format(user_id))
                                            elif '加入' in message[1]:
                                                name = message[2]
                                                if name not in long:
                                                    send_group_message(group, '[CQ:at,qq={}] 没有这个接龙名称！'.format(user_id))
                                                else:
                                                    long[name].append(request_get_json['sender']['nickname'])
                                                    print(long[name])
                                                    send_group_message(group, '[CQ:at,qq={}] 接龙成功！'.format(user_id))
                                            elif '结束' in message[1]:
                                                name = message[2]
                                                if name not in long:
                                                    send_group_message(group, '[CQ:at,qq={}] 没有这个接龙名称！'.format(user_id))
                                                else:
                                                    send_group_message(group,
                                                                       '[CQ:at,qq={}] 接龙结束！接龙结果：{}'.format(user_id,
                                                                                                                   long[
                                                                                                                       name]))
                                                    del long[name]
                                        elif '天气查询' == message[1]:
                                            if message[2] == '官方':
                                                url = 'http://t.weather.sojson.com/api/weather/city/'
                                                city = message[3]
                                                f = open('city.json', 'rb')
                                                cities = load(f)
                                                city_get = cities.get(city)
                                                response = req.get(url + city_get)
                                                d = response.json()
                                                if d['status'] == 200:
                                                    send_group_message(group,
                                                                       '[CQ:at,qq={}]\n城市：{}\n时间{}\n温度：{}\n天气：{}\n'.format(
                                                                           user_id,
                                                                           (d["cityInfo"]["parent"], d["cityInfo"]["city"]),
                                                                           (d["time"], d["data"]["forecast"][0]["week"]), (
                                                                               d["data"]["forecast"][0]["high"],
                                                                               d["data"]["forecast"][0]["low"]),
                                                                           d["data"]["forecast"][0]["type"]))
                                            elif message[2] == '高德':
                                                workbook = xlrd.open_workbook(
                                                    r'D:\pythonproject\3000_lines_code\qq群机器人\acode.xlsx')
                                                string = message[3]
                                                num = 0
                                                sheet = workbook.sheet_by_index(0)
                                                first_col = sheet.col_values(0)
                                                sec_col = sheet.col_values(1)
                                                for f in first_col:
                                                    if f == string:
                                                        break
                                                    num += 1
                                                cont = list(sec_col)[num]
                                                json = req.get('https://restapi.amap.com/v3/weather/weatherInfo?city={}&key='.format(cont))#在key选项中填入你的key
                                                print(json.json())
                                                content = '城市为：{}\n天气为：{}\n温度为：{}\n风向为：{}\n风级为：{}\n时间：{}'.format(json.json()['lives'][0]['province'], json.json()['lives'][0]['weather'], json.json()['lives'][0]['temperature_float'], json.json()['lives'][0]['winddirection'], json.json()['lives'][0]['windpower'], json.json()['lives'][0]['reporttime'])
                                                send_group_message(group, '[CQ:at,qq={}] {}'.format(user_id, content))
                                            else:
                                                url = 'http://t.weather.sojson.com/api/weather/city/'
                                                city = message[3]
                                                f = open('city.json', 'rb')
                                                cities = load(f)
                                                city_get = cities.get(city)
                                                response = req.get(url + city_get)
                                                d = response.json()
                                                if d['status'] == 200:
                                                    send_group_message(group,
                                                                       '[CQ:at,qq={}]\n城市：{}\n时间{}\n温度：{}\n天气：{}\n'.format(
                                                                           user_id,
                                                                           (d["cityInfo"]["parent"],
                                                                            d["cityInfo"]["city"]),
                                                                           (
                                                                           d["time"], d["data"]["forecast"][0]["week"]),
                                                                           (
                                                                               d["data"]["forecast"][0]["high"],
                                                                               d["data"]["forecast"][0]["low"]),
                                                                           d["data"]["forecast"][0]["type"]))
                                        elif message[1] == '生成二维码':
                                            try:
                                                message = message_.split(' ')
                                                qr = QRCode(version=message[3], error_correction=ERROR_CORRECT_H,
                                                            box_size=message[4], border=message[5])
                                                qr.add_data(message[2])
                                                qr.make(message[6])
                                                img = qr.make_image(fill_color=message[7], back_color=message[8])
                                                with open(
                                                        r'D:\pythonproject\3000_lines_code\qq群机器人\cqhttp\data\images\qrcode.png',
                                                        'wb') as f:
                                                    img.save(f)
                                                    f.close()
                                                send_group_message(group, r'生成成功！图片[CQ:image,file=qrcode.png]')
                                            except IndexError:
                                                qr = QRCode(version=1, error_correction=ERROR_CORRECT_H,
                                                            box_size=10, border=4)
                                                qr.add_data(message[2])
                                                qr.make()
                                                img = qr.make_image(fill_color="orange", back_color="red")
                                                with open(
                                                        r'D:\pythonproject\3000_lines_code\qq群机器人\cqhttp\data\images\qrcode.png',
                                                        'wb') as f:
                                                    img.save(f)
                                                    f.close()
                                                send_group_message(group, r'生成成功！图片[CQ:image,file=qrcode.png]')
                                        elif message[1] == '撤回消息':
                                            delete_group_message()
                                           '''
                                        elif message[1] == '加密':
                                            message = message_.split(' ', 2)
                                            string = message[2]
                                            string_en = parse.quote(string)
                                            print(string_en)
                                            e = Encode(code=CODE)
                                            new = e.encode(string_en)
                                            send_group_message(group, '[CQ:at,qq={}] 密文：{}'.format(user_id, new))
                                        elif message[1] == '解密':
                                            message = message_.split(' ', 2)
                                            num = int(message[2])
                                            d = Decode(code=CODE)
                                            string_de = d.decode(num)
                                            new = parse.unquote(string_de)
                                            print(string_de)
                                            send_group_message(group, '[CQ:at,qq={}] 明文：{}'.format(user_id, new))
                                            '''# 本段代码有问题，请自行解决
                                        elif message[1] == 'chat':
                                            if user_id in chat_gpt_list:
                                                try:
                                                    prompt = message[2]
                                                    answer = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=1, max_tokens=int(message[3]),frequency_penalty=0, presence_penalty=0)["choices"][0]["text"].strip()
                                                    send_group_message(group, '[CQ:at,qq={}] 回答：{}'.format(user_id, answer))
                                                except IndexError:
                                                    prompt = message[2]
                                                    answer = openai.Completion.create(model="text-davinci-003", prompt=prompt,temperature=1, max_tokens=100,frequency_penalty=0, presence_penalty=0)["choices"][0]["text"].strip()
                                                    send_group_message(group, '[CQ:at,qq={}] 回答：{}'.format(user_id, answer))
                                            else:
                                                send_group_message(group, '[CQ:at,qq={}] 你没有权限！'.format(user_id))
                                        elif message[1] == '生成图片':
                                            if user_id in summon_images_list:
                                                try:
                                                    prompt = message[2]
                                                    image = openai.Image.create(prompt=prompt,
                                                                                n=3,
                                                                                model="image-alpha-001",
                                                                                size=message[3],
                                                                                response_format="url")

                                                    # 第一张图片
                                                    image_rul = image["data"][0]["url"]
                                                    res = req.get(image_rul)
                                                    f = open(
                                                        file=r'', #改为你的路径
                                                        mode='wb')
                                                    f.write(res.content)
                                                    f.close()
                                                    send_group_message(group,
                                                                       '[CQ:at,qq={}] 生成成功！[CQ:image,file=image.jpg]'.format(
                                                                           user_id))
                                                except IndexError:
                                                    prompt = message[2]
                                                    image = openai.Image.create(prompt=prompt,
                                                                                n=3,
                                                                                model="image-alpha-001",
                                                                                size='256x256',
                                                                                response_format="url")

                                                    # 第一张图片
                                                    image_rul = image["data"][0]["url"]
                                                    res = req.get(image_rul)
                                                    f = open(
                                                        file=r'',#改为你的路径
                                                        mode='wb')
                                                    f.write(res.content)
                                                    f.close()
                                                    send_group_message(group,
                                                                       '[CQ:at,qq={}] 生成成功！[CQ:image,file=image.jpg]'.format(
                                                                           user_id))
                                                else:
                                                    send_group_message(group, '[CQ:at,qq={}] 你没有权限！'.format(user_id))
                                        elif message[1] == '赞助':
                                            if message[2] == '微信':
                                                send_group_message(group,
                                                                   ''.format(# 改为你的赞助吗
                                                                       user_id))
                                            if message[2] == 'QQ' or message[2] == 'qq':
                                                send_group_message(group,
                                                                   ''.format(# 改为你的赞助码
                                                                       user_id))
                                        elif message[1] == '反馈':
                                            content = message[2]
                                            with open(file='反馈.txt', mode='a+', encoding='utf-8') as f:
                                                f.write(content + '\n')
                                                f.close()
                                            send_group_message(group, '[CQ:at,qq={}] 已成功反馈至作者电脑！感谢您的反馈！'.format(
                                                user_id))
                                        elif message[1] == '点歌':
                                            name = message[2]
                                            song = diange(name)
                                            send_group_message(group, song)
                                        elif message[1] == '搜索github项目':
                                            json = req.get('https://api.github.com/search/repositories?q={}'.format(message[2]))
                                            send_group_message(group, '[CQ:at,qq={}] 名称{}，网址{}'.format(user_id, json.json()['items'][0]['name'],
                                                                         json.json()['items'][0]['html_url']))
                                        elif message[1] == 'ip' or message[1] == 'IP':
                                            ip = message[2]
                                            json = req.get(
                                                'https://restapi.amap.com/v3/ip?ip={}&output=json&key='.format(ip))#在key中改为你的key
                                            cmd_output = []
                                            ping = Popen('ping {}'.format(ip), stdout=PIPE, shell=True, close_fds=True)
                                            cmd_res['out'] = ping.stdout.readlines()
                                            for temp in cmd_res['out']:
                                                cmd_output.append(temp.decode('gbk'))
                                            for temp in range(len(cmd_output)):
                                                cmd_output[temp] = cmd_output[temp].replace('\r\n', '    ')
                                            send_group_message(group,
                                                               '[CQ:at,qq={}] 高德：{}\nping:{}'.format(
                                                                   user_id, json.json()['province'], cmd_output))
                                        elif message[1] == '随机听歌':
                                            url = 'https://api.wqwlkj.cn/wqwlapi/wyy_random.php?type=json'
                                            netease = requests.get(url)
                                            netease_wyy = loads(netease.text)
                                            text = netease_wyy['data']
                                            netease_id = text['id']
                                            send_group_message(group, '[CQ:music,type=163,id={}]'.format(netease_id))
                                        elif message[1] == 'up信息':
                                            name = message[2]
                                            json = req.get('https://api.bilibili.com/x/web-interface/wbi/search/type?page=1&keyword={}&search_type=bili_user'.format(name))
                                            send_group_message(group, f'[CQ:at,qq={user_id}]搜索结果：\n用户名：{json.json()["data"]["result"][0]["uname"]}\nmid:{json.json()["data"]["result"][0]["mid"]}\n签名：{json.json()["data"]["result"][0]["usign"]}\n粉丝：{json.json()["data"]["result"][0]["fans"]}\n视频数量：{json.json()["data"]["result"][0]["videos"]}\n等级：{json.json()["data"]["result"][0]["level"]}\n以下是最新视频的内容：\naid:{json.json()["data"]["result"][0]["res"][0]["aid"]}\nbid:{json.json()["data"]["result"][0]["res"][0]["bvid"]}\n硬币：{json.json()["data"]["result"][0]["res"][0]["coin"]}\n标题：{json.json()["data"]["result"][0]["res"][0]["title"]}\n简介：{json.json()["data"]["result"][0]["res"][0]["desc"]}')
                                        elif 'group' in message[1]:
                                            if user_id in group_admin_list:
                                                if '踢人' == message[2]:
                                                    id = message[3]
                                                    req.get('http://127.0.0.1:5700/set_group_kick?group_id={}&user_id={}'.format(group, id))
                                                    send_group_message(group, '[CQ:at,qq={}] 成功！如果不成功的话请联系@小井井'.format(user_id))
                                                elif '禁言' == message[2]:
                                                    id = message[3]
                                                    time = message[4]
                                                    req.get('http://127.0.0.1:5700/set_group_ban?group_id={}&user_id={}&duration={}'.format(group, id, time))
                                                    send_group_message(group, '[CQ:at,qq={}] 成功！如果不成功的话请联系@小井井'.format(user_id))
                                                elif '禁言匿名' == message[2]:
                                                    time = message[3]
                                                    req.get('http://127.0.0.1:5700/set_group_anonymous_ban?group_id={}&duration={}'.format(group, time))
                                                    send_group_message(group, '[CQ:at,qq={}] 成功！如果不成功的话请联系@小井井'.format(user_id))
                                                elif '全员禁言' == message[2]:
                                                    pan = message[3]
                                                    req.get('http://127.0.0.1:5700/set_group_whole_ban?group_id={}enable={}'.format(group, pan))
                                                    send_group_message(group, '[CQ:at,qq={}] 成功！如果不成功的话请联系@小井井'.format(user_id))
                                            else:
                                                send_group_message(group, '[CQ:at,qq={}] 你没有权限！'.format(user_id))
                                        elif 'code' in message[1]:
                                            # 命令功能
                                            if user_id in adminlist:
                                                if 'blacklist' in message[1]:
                                                    if 'append' in message[2]:
                                                        if int(message[3]) not in blacklist:
                                                            blacklist.append(int(message[3]))
                                                            send_group_message(group, '[CQ:at,qq={}] blacklist{}'.format(
                                                                user_id, blacklist))
                                                    elif 'remove' in message[2]:
                                                        blacklist.remove(int(message[3]))
                                                        send_group_message(group, '[CQ:at,qq={}] blacklist{}'.format(
                                                            user_id, blacklist))
                                                    elif 'save' in message[2]:
                                                        with open(file='black_list.txt', mode='w+', encoding='utf-8') as f:
                                                            f.write(str(blacklist))
                                                            f.close()
                                                        send_group_message(group,
                                                                           '[CQ:at,qq={}] {}'.format(user_id,
                                                                                                     '保存成功！blacklist{}'.format(
                                                                                                         blacklist)))
                                                    elif 'show' in message[2]:
                                                        send_group_message(group, 'blacklist{}'.format(blacklist))
                                                    else:
                                                        send_group_message(group, '[CQ:at,qq={}] 无效的指令！'.format(user_id))
                                                elif 'adminlist' in message[1]:
                                                    if 'append' in message[2]:
                                                        if int(message[3]) not in adminlist:
                                                            adminlist.append(int(message[3]))
                                                            send_group_message(group,
                                                                               '[CQ:at,qq={}] adminlist{}'.format(user_id,
                                                                                                                  adminlist))
                                                    elif 'remove' in message[2]:
                                                        adminlist.remove(int(message[3]))
                                                        send_group_message(group,
                                                                           '[CQ:at,qq={}] adminlist{}'.format(user_id,
                                                                                                              adminlist))
                                                    elif 'save' in message[2]:
                                                        with open(file='admin_list.txt', mode='w+', encoding='utf-8') as f:
                                                            f.write(str(adminlist))
                                                            f.close()
                                                        send_group_message(group,
                                                                           '[CQ:at,qq={}] 保存成功！adminlist{}'.format(user_id,
                                                                                                                       adminlist))
                                                    elif 'show' in message[2]:
                                                        send_group_message(group, 'adminlist{}'.format(adminlist))
                                                    else:
                                                        send_group_message(group, '[CQ:at,qq={}] 无效的指令！'.format(user_id))
                                                elif '运行python' in message[1]:
                                                    # 运行代码功能
                                                    with open(file=r'.\run_command.py', mode='w+', encoding='utf-8') as f:
                                                        try:
                                                            f.write('from math import *\nfrom 机器人 import *\n')
                                                            f.write(message[2] + ' ' + message[3] + ' ' + message[4])
                                                        except IndexError:
                                                            try:
                                                                f.write(message[2] + ' ' + message[3])
                                                            except IndexError:
                                                                f.write(message[2])
                                                        finally:
                                                            f.close()
                                                    string = r''#改为你的路径
                                                    cmd_output = []
                                                    cmd_error = []
                                                    run = Popen(string, stderr=PIPE, stdout=PIPE, close_fds=True, shell=True)
                                                    cmd_res['out'] = run.stdout.readlines()
                                                    cmd_res['error'] = run.stderr.readlines()
                                                    for temp in cmd_res['out']:
                                                        cmd_output.append(temp.decode('utf-8'))
                                                    for temp in cmd_res['error']:
                                                        cmd_error.append(temp.decode('utf-8'))
                                                    send_group_message(request_get_json['group_id'],
                                                                       '[CQ:at,qq={}] 运行结果：\n输出：{}，\n错误：{}'.format(
                                                                           user_id, cmd_output, cmd_error))
                                                elif 'OPonly' in message[1]:
                                                    set = message[2]
                                                    if set == 'True':
                                                        OPonly = True
                                                        send_group_message(group,
                                                                           '[CQ:at,qq={}] OPonly{}'.format(user_id, OPonly))
                                                    if set == 'False':
                                                        OPonly = False
                                                        send_group_message(group,
                                                                           '[CQ:at,qq={}] OPonly{}'.format(user_id, OPonly))
                                                    else:
                                                        send_group_message(group, '[CQ:at,qq={}] 无效的指令！'.format(user_id))
                                                elif 'pythonlist' in message[1]:
                                                    if 'append' in message[2]:
                                                        if int(message[3]) not in python_list:
                                                            python_list.append(int(message[3]))
                                                            send_group_message(group,
                                                                               '[CQ:at,qq={}] pythonlist{}'.format(user_id,
                                                                                                                   python_list))
                                                    elif 'remove' in message[2]:
                                                        python_list.remove(int(message[3]))
                                                        send_group_message(group,
                                                                           '[CQ:at,qq={}] pythonlist{}'.format(user_id,
                                                                                                               python_list))
                                                    elif 'save' in message[2]:
                                                        with open(file='can_use_python_list.txt', mode='w+',
                                                                  encoding='utf-8') as f:
                                                            f.write(str(python_list))
                                                            f.close()
                                                        send_group_message(group,
                                                                           '[CQ:at,qq={}] 保存成功！pythonlist{}'.format(user_id,
                                                                                                                        python_list))
                                                    elif 'show' in message[2]:
                                                        send_group_message(group, 'pythonlist{}'.format(python_list))
                                                    else:
                                                        send_group_message(group, '[CQ:at,qq={}] 无效的指令！'.format(user_id))
                                                elif 'chatgptlist' in message[1]:
                                                    if 'append' in message[2]:
                                                        if int(message[3]) not in chat_gpt_list:
                                                            chat_gpt_list.append(int(message[3]))
                                                            send_group_message(group,
                                                                               '[CQ:at,qq={}] chatgptlist{}'.format(user_id,
                                                                                                                    chat_gpt_list))
                                                    elif 'remove' in message[2]:
                                                        chat_gpt_list.remove(int(message[3]))
                                                        send_group_message(group,
                                                                           '[CQ:at,qq={}] chatgptlist{}'.format(user_id,
                                                                                                                chat_gpt_list))
                                                    elif 'save' in message[2]:
                                                        with open(file='chat_gpt_list.txt', mode='w+',
                                                                  encoding='utf-8') as f:
                                                            f.write(str(chat_gpt_list))
                                                            f.close()
                                                        send_group_message(group,
                                                                           '[CQ:at,qq={}] 保存成功！chatgptlist{}'.format(
                                                                               user_id,
                                                                               chat_gpt_list))
                                                    elif 'show' in message[2]:
                                                        send_group_message(group, 'chatgptlist{}'.format(chat_gpt_list))
                                                    else:
                                                        send_group_message(group, '[CQ:at,qq={}] 无效的指令！'.format(user_id))
                                                elif 'summonimage' in message[1]:
                                                    if 'append' in message[2]:
                                                        if int(message[3]) not in summon_images_list:
                                                            summon_images_list.append(int(message[3]))
                                                            send_group_message(group,
                                                                               '[CQ:at,qq={}] summonimageslist{}'.format(user_id,
                                                                                                                    summon_images_list))
                                                    elif 'remove' in message[2]:
                                                        summon_images_list.remove(int(message[3]))
                                                        send_group_message(group,
                                                                           '[CQ:at,qq={}] summonimageslist{}'.format(user_id,
                                                                                                                summon_images_list))
                                                    elif 'save' in message[2]:
                                                        with open(file='summon_images_list.txt', mode='w+',
                                                                  encoding='utf-8') as f:
                                                            f.write(str(summon_images_list))
                                                            f.close()
                                                        send_group_message(group,
                                                                           '[CQ:at,qq={}] 保存成功！summonimageslist{}'.format(
                                                                               user_id,
                                                                               summon_images_list))
                                                    elif 'show' in message[2]:
                                                        send_group_message(group, 'summonimageslist{}'.format(summon_images_list))
                                                    else:
                                                        send_group_message(group, '[CQ:at,qq={}] 无效的指令！'.format(user_id))
                                                elif 'groupadminlist' in message[1]:
                                                    if 'append' in message[2]:
                                                        if int(message[3]) not in group_admin_list:
                                                            group_admin_list.append(int(message[3]))
                                                            send_group_message(group,
                                                                               '[CQ:at,qq={}] groupadminlist{}'.format(user_id,
                                                                                                                    group_admin_list))
                                                    elif 'remove' in message[2]:
                                                        group_admin_list.remove(int(message[3]))
                                                        send_group_message(group,
                                                                           '[CQ:at,qq={}] groupadminlist{}'.format(user_id,
                                                                                                                group_admin_list))
                                                    elif 'save' in message[2]:
                                                        with open(file='group_admin_list.txt', mode='w+',
                                                                  encoding='utf-8') as f:
                                                            f.write(str(group_admin_list))
                                                            f.close()
                                                        send_group_message(group,
                                                                           '[CQ:at,qq={}] 保存成功！groupadminlist{}'.format(
                                                                               user_id,
                                                                               group_admin_list))
                                                    elif 'show' in message[2]:
                                                        send_group_message(group, 'groupadminlist{}'.format(group_admin_list))
                                                    else:
                                                        send_group_message(group, '[CQ:at,qq={}] 无效的指令！'.format(user_id))
                                                elif 'clist' in message[1]:
                                                    if 'append' in message[2]:
                                                        if int(message[3]) not in c_list:
                                                            c_list.append(int(message[3]))
                                                            send_group_message(group,
                                                                               '[CQ:at,qq={}] clist{}'.format(user_id,
                                                                                                                   c_list))
                                                    elif 'remove' in message[2]:
                                                        c_list.remove(int(message[3]))
                                                        send_group_message(group,
                                                                           '[CQ:at,qq={}] clist{}'.format(user_id,
                                                                                                               c_list))
                                                    elif 'save' in message[2]:
                                                        with open(file='can_use_c_list.txt', mode='w+',
                                                                  encoding='utf-8') as f:
                                                            f.write(str(c_list))
                                                            f.close()
                                                        send_group_message(group,
                                                                           '[CQ:at,qq={}] 保存成功！clist{}'.format(user_id,
                                                                                                                        c_list))
                                                    elif 'show' in message[2]:
                                                        send_group_message(group, 'pythonlist{}'.format(c_list))
                                                    else:
                                                        send_group_message(group, '[CQ:at,qq={}] 无效的指令！'.format(user_id))
                                                elif 'javalist' in message[1]:
                                                    if 'append' in message[2]:
                                                        if int(message[3]) not in java_list:
                                                            java_list.append(int(message[3]))
                                                            send_group_message(group,
                                                                               '[CQ:at,qq={}] javalist{}'.format(user_id,
                                                                                                                   java_list))
                                                    elif 'remove' in message[2]:
                                                        java_list.remove(int(message[3]))
                                                        send_group_message(group,
                                                                           '[CQ:at,qq={}] javalist{}'.format(user_id,
                                                                                                               java_list))
                                                    elif 'save' in message[2]:
                                                        with open(file='can_use_java_list.txt', mode='w+',
                                                                  encoding='utf-8') as f:
                                                            f.write(str(java_list))
                                                            f.close()
                                                        send_group_message(group,
                                                                           '[CQ:at,qq={}] 保存成功！javalist{}'.format(user_id,
                                                                                                                      java_list))
                                                    elif 'show' in message[2]:
                                                        send_group_message(group, 'javalist{}'.format(java_list))
                                                    else:
                                                        send_group_message(group, '[CQ:at,qq={}] 无效的指令！'.format(user_id))
                                                elif 'autosave' in message[1]:
                                                    if 'set' in message[2]:
                                                        autosave = bool(message[3])
                                                        send_group_message(group,
                                                                           '[CQ:at,qq={}] autosave{}'.format(user_id,
                                                                                                              autosave))
                                                    elif 'show' in message[2]:
                                                        send_group_message(group, 'autosave{}'.format(autosave))
                                                else:
                                                    send_group_message(group, '[CQ:at,qq={}] 无效的指令！'.format(user_id))
                                            else:
                                                send_group_message(group, '[CQ:at,qq={}] 你没有权限！'.format(user_id))
                                        else:
                                            # 其他功能
                                            send_group_message(group,
                                                               '[CQ:at,qq={}] 你说什么呢？'.format(
                                                                   user_id))
                                    else:
                                        send_group_message(group, '[CQ:at,qq={}] 管理员已禁用！'.format(user_id))
                                else:
                                    send_group_message(request_get_json['group_id'], '[CQ:at,qq={}] 你没有权限!请跟@小井井'
                                                                                         '联系并索取！'.format(
                                            user_id))
                        except Exception as e:
                            send_group_message(group, '[CQ:at,qq={}] 发生错误：{}！'.format(user_id, str(e)))
                            raise
                    elif request_get_json['message_type'] == 'private':
                        #本段功能并未完善，可以抄着上面的去增加功能
                        print(request_get_json)
                        message_ = request_get_json['message']
                        user_id = request_get_json['sender']['user_id']
                        message = message_.split(' ', 3)
                        print(message)
                        if '你好' == message[0]:
                            # 你好功能
                            send_private_message(user_id,
                                               'hello')
                        elif '功能' == message[0]:
                            # 功能功能
                            send_private_message(user_id, 'hello\n功能1：你好打招呼功能\n功能2：查询功能功能\n功能3'
                                                      '：运行python'
                                                      '功能4：查询天气\n功能5：生成二维码\n功能6'
                                                      '：撤回消息（无消息）\n功能7：加/解密\n功能8：chatgpt'
                                                      '问答（作者申请了好久的账号，给点赞助吧！）\n功能9：赞助\n功能10：反馈')
                        elif '查询功能' == message[0]:
                            pass
                        elif message[0] == '运行python':
                            # 运行代码功能
                            with open(file=r'.\run_command.py', mode='w+', encoding='utf-8') as f:
                                message = message_.split(' ', 2)
                                f.write(message[2])
                                f.close()
                            with open(file=r'.\run_command.py', mode='r+', encoding='utf-8') as f:
                                r = f.read()
                                f.close()
                            if 'os' in r:
                                send_private_message(user_id,
                                                   '您的代码中有敏感词！os')
                            elif 'subprocess' in r:
                                send_private_message(user_id,
                                                   '您的代码中有敏感词！subprocess')
                            elif 'commands' in r:
                                send_private_message(user_id,
                                                   '您的代码中有敏感词！commands')
                            else:
                                string = ' {}'.format(
                                                        r'')#改为你的路径
                                cmd_output = []
                                cmd_error = []
                                run = Popen(string, stderr=PIPE, stdout=PIPE, close_fds=True, shell=True)
                                cmd_res['out'] = run.stdout.readlines()
                                cmd_res['error'] = run.stderr.readlines()
                                for temp in cmd_res['out']:
                                    cmd_output.append(temp.decode('gbk'))
                                for temp in cmd_res['error']:
                                    cmd_error.append(temp.decode('gbk'))
                                for temp in range(len(cmd_error)):
                                    cmd_error[temp] = cmd_error[temp].replace('\r\n', '    ')
                                for temp in range(len(cmd_output)):
                                    cmd_output[temp] = cmd_output[temp].replace('\r\n', '    ')
                                send_private_message(user_id,
                                                   '运行结果：\n输出：{}，\n错误：{}'.format(cmd_output, cmd_error))
                        elif message[1] == '运行java':
                            with open(file=r'.\Main.java', mode='w+', encoding='utf-8') as f:
                                message = message_.split(' ', 2)
                                f.write(message[2])
                                f.close()
                            string = r''#改为你的路径
                            cmd_output = []
                            cmd_error = []
                            run = Popen(string, stderr=PIPE, stdout=PIPE, close_fds=True, shell=True)
                            cmd_res['out'] = run.stdout.readlines()
                            cmd_res['error'] = run.stderr.readlines()
                            for temp in cmd_res['out']:
                                cmd_output.append(temp.decode('gbk'))
                            for temp in cmd_res['error']:
                                cmd_error.append(temp.decode('gbk'))
                            for temp in range(len(cmd_error)):
                                cmd_error[temp] = cmd_error[temp].replace('\r\n', '    ')
                            for temp in range(len(cmd_output)):
                                cmd_output[temp] = cmd_output[temp].replace('\r\n', '    ')
                            send_private_message(user_id,
                                               '运行结果：\n输出：{}，\n错误：{}'.format(cmd_output, cmd_error))
                        elif message[1] == '运行c':
                            with open(file=r'.\library.c', mode='w+', encoding='utf-8') as f:
                                message = message_.split(' ', 2)
                                f.write(message[2])
                                f.close()
                            string = r''#改为你的路径
                            cmd_output = []
                            cmd_error = []
                            run = Popen(string, stderr=PIPE, stdout=PIPE, close_fds=True, shell=True)
                            cmd_res['out'] = run.stdout.readlines()
                            cmd_res['error'] = run.stderr.readlines()
                            for temp in cmd_res['out']:
                                cmd_output.append(temp.decode('gbk'))
                            for temp in cmd_res['error']:
                                cmd_error.append(temp.decode('gbk'))
                            for temp in range(len(cmd_error)):
                                cmd_error[temp] = cmd_error[temp].replace('\r\n', '    ')
                            for temp in range(len(cmd_output)):
                                cmd_output[temp] = cmd_output[temp].replace('\r\n', '    ')
                            send_private_message(user_id,
                                               '编译结果：\n输出：{}，\n错误：{}'.format(cmd_output, cmd_error))
                            string = r''#改为你的路径
                            cmd_output = []
                            cmd_error = []
                            run = Popen(string, stderr=PIPE, stdout=PIPE, close_fds=True, shell=True)
                            cmd_res['out'] = run.stdout.readlines()
                            cmd_res['error'] = run.stderr.readlines()
                            for temp in cmd_res['out']:
                                cmd_output.append(temp.decode('utf-8'))
                            for temp in cmd_res['error']:
                                cmd_error.append(temp.decode('utf-8'))
                            send_private_message(user_id,
                                               '运行结果：\n输出：{}，\n错误：{}'.format(cmd_output, cmd_error))
                        elif '天气查询' == message[0]:
                            url = 'http://t.weather.sojson.com/api/weather/city/'
                            city = message[1]
                            f = open('city.json', 'rb')
                            cities = load(f)
                            city = cities.get(city)
                            response = req.get(url + city)
                            d = response.json()
                            if d['status'] == 200:
                                send_private_message(user_id,
                                                   '城市：{}\n时间{}\n温度：{}\n天气：{}\n'.format(
                                                       (d["cityInfo"]["parent"], d["cityInfo"]["city"]),
                                                       (d["time"], d["data"]["forecast"][0]["week"]), (
                                                           d["data"]["forecast"][0]["high"],
                                                           d["data"]["forecast"][0]["low"]),
                                                       d["data"]["forecast"][0]["type"]))
                        elif message[0] == '生成二维码':
                            try:
                                message = message_.split(' ')
                                qr = QRCode(version=message[2], error_correction=ERROR_CORRECT_H,
                                            box_size=message[3], border=message[4])
                                qr.add_data(message[1])
                                qr.make(message[5])
                                img = qr.make_image(fill_color=message[6], back_color=message[7])
                                with open(
                                        r'D:\pythonproject\3000_lines_code\qq群机器人\cqhttp\data\images\qrcode.png',
                                        'wb') as f:
                                    img.save(f)
                                    f.close()
                                send_private_message(user_id, r'生成成功！图片[CQ:image,file=qrcode.png]')
                            except IndexError:
                                qr = QRCode(version=1, error_correction=ERROR_CORRECT_H,
                                            box_size=10, border=4)
                                qr.add_data(message[1])
                                qr.make()
                                img = qr.make_image(fill_color="orange", back_color="red")
                                with open(
                                        r'',#改为你的路径
                                        'wb') as f:
                                    img.save(f)
                                    f.close()
                                send_private_message(user_id, r'生成成功！图片[CQ:image,file=qrcode.png]')
                        elif message[0] == '撤回消息':
                            delete_private_message()
                        elif message[0] == '查询音乐':
                            pass
                        '''
                        elif message[0] == '加密':
                            message = message_.split(' ', 2)
                            string = message[1]
                            string_en = parse.quote(string)
                            print(string_en)
                            e = Encode(code=CODE)
                            new = e.encode(string_en)
                            send_private_message(user_id, '密文：{}'.format(new))
                        elif message[0] == '解密':
                            message = message_.split(' ', 2)
                            num = int(message[1])
                            d = Decode(code=CODE)
                            string_de = d.decode(num)
                            new = parse.unquote(string_de)
                            print(string_de)
                            send_private_message(user_id, '明文：{}'.format(new))
                            '''#本段代码有问题，请自行解决
                        elif message[0] == 'chat':
                            try:
                                prompt = message[1]
                                answer = \
                                openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=1,
                                                         max_tokens=int(message[2]), frequency_penalty=0,
                                                         presence_penalty=0)["choices"][0]["text"].strip()
                                send_private_message(user_id, '回答：{}'.format(answer))
                            except IndexError:
                                prompt = message[1]
                                answer = \
                                openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=1,
                                                         max_tokens=100, frequency_penalty=0, presence_penalty=0)[
                                    "choices"][0]["text"].strip()
                                send_private_message(user_id, '回答：{}'.format(answer))
                        elif message[1] == '生成图片':
                            try:
                                prompt = message[1]
                                image = openai.Image.create(prompt=prompt,
                                                            n=3,
                                                            model="image-alpha-001",
                                                            size=message[2],
                                                            response_format="url")

                                # 第一张图片
                                image_rul = image["data"][0]["url"]
                                res = req.get(image_rul)
                                f = open(
                                    file=r'D:\pythonproject\3000_lines_code\qq群机器人\cqhttp\data\images\image.jpg',
                                    mode='wb')
                                f.write(res.content)
                                f.close()
                                send_private_message(user_id,
                                                   '生成成功！[CQ:image,file=image.jpg]')
                            except IndexError:
                                prompt = message[1]
                                image = openai.Image.create(prompt=prompt,
                                                            n=3,
                                                            model="image-alpha-001",
                                                            size='256x256',
                                                            response_format="url")

                                # 第一张图片
                                image_rul = image["data"][0]["url"]
                                res = req.get(image_rul)
                                f = open(
                                    file=r'D:\pythonproject\3000_lines_code\qq群机器人\cqhttp\data\images\image.jpg',
                                    mode='wb')
                                f.write(res.content)
                                f.close()
                                send_private_message(user_id,
                                                   '生成成功！[CQ:image,file=image.jpg]')
                        elif message[0] == '赞助':
                            if message[1] == '微信':
                                send_private_message(user_id,
                                                   '[CQ:image,file=weixinpay.png]求求赞助一下吧！')
                            if message[1] == 'QQ' or message[1] == 'qq':
                                send_private_message(user_id,
                                                   '[CQ:image,file=qqpay.png]求求赞助一下吧！')
                        elif message[0] == '反馈':
                            content = message[1]
                            with open(file='反馈.txt', mode='a+', encoding='utf-8') as f:
                                f.write(content + '\n')
                                f.close()
                            send_private_message(user_id, '已成功反馈至作者电脑！感谢您的反馈！')
            except Exception as e:
                raise
            with open(file='black_list.txt', mode='r+', encoding='utf-8') as f:
                try:
                    blacklist = list(f.readlines())
                    blacklist = blacklist[0][1:-1].split(',')
                    for temp in range(len(blacklist)):
                        blacklist[temp] = int(blacklist[temp])
                except (IndexError, ValueError):
                    blacklist = []
                finally:
                    f.close()
            with open(file='admin_list.txt', mode='r+', encoding='utf-8') as f:
                try:
                    adminlist = list(f.readlines())
                    adminlist = adminlist[0][1:-1].split(',')
                    for temp in range(len(adminlist)):
                        adminlist[temp] = int(adminlist[temp])
                except (IndexError, ValueError):
                    adminlist = []
                finally:
                    f.close()
            with open(file='can_use_python_list.txt', mode='r+', encoding='utf-8') as f:
                try:
                    python_list = list(f.readlines())
                    python_list = python_list[0][1:-1].split(',')
                    for temp in range(len(python_list)):
                        python_list[temp] = int(python_list[temp])
                except (IndexError, ValueError):
                    python_list = []
                finally:
                    f.close()
            with open(file='chat_gpt_list.txt', mode='r+', encoding='utf-8') as f:
                try:
                    chat_gpt_list = list(f.readlines())
                    chat_gpt_list = chat_gpt_list[0][1:-1].split(',')
                    for temp in range(len(chat_gpt_list)):
                        chat_gpt_list[temp] = int(chat_gpt_list[temp])
                except (IndexError, ValueError):
                    chat_gpt_list = []
                finally:
                    f.close()
            with open(file='summon_images_list.txt', mode='r+', encoding='utf-8') as f:
                try:
                    summon_images_list = list(f.readlines())
                    summon_images_list = summon_images_list[0][1:-1].split(',')
                    for temp in range(len(summon_images_list)):
                        summon_images_list[temp] = int(summon_images_list[temp])
                except (IndexError, ValueError):
                    summon_images_list = []
                finally:
                    f.close()
            with open(file='group_admin_list.txt', mode='r+', encoding='utf-8') as f:
                try:
                    group_admin_list = list(f.readlines())
                    group_admin_list = group_admin_list[0][1:-1].split(',')
                    for temp in range(len(group_admin_list)):
                        group_admin_list[temp] = int(group_admin_list[temp])
                except (IndexError, ValueError):
                    group_admin_list = []
                finally:
                    f.close()
            with open(file='can_use_java_list.txt', mode='r+', encoding='utf-8') as f:
                try:
                    java_list = list(f.readlines())
                    java_list = java_list[0][1:-1].split(',')
                    for temp in range(len(java_list)):
                        java_list[temp] = int(java_list[temp])
                except (IndexError, ValueError):
                    java_list = []
                finally:
                    f.close()
            with open(file='can_use_c_list.txt', mode='r+', encoding='utf-8') as f:
                try:
                    c_list = list(f.readlines())
                    c_list = c_list[0][1:-1].split(',')
                    for temp in range(len(c_list)):
                        c_list[temp] = int(c_list[temp])
                except (IndexError, ValueError):
                    c_list = []
                finally:
                    f.close()
            if autosave:
                with open(file='can_use_java_list.txt', mode='w+',
                          encoding='utf-8') as f:
                    f.write(str(java_list))
                    f.close()
                with open(file='can_use_c_list.txt', mode='w+',
                          encoding='utf-8') as f:
                    f.write(str(java_list))
                    f.close()
                with open(file='can_use_python_list.txt', mode='w+',
                          encoding='utf-8') as f:
                    f.write(str(java_list))
                    f.close()
                with open(file='group_admin_list.txt', mode='w+',
                          encoding='utf-8') as f:
                    f.write(str(java_list))
                    f.close()
                with open(file='black_list.txt', mode='w+',
                          encoding='utf-8') as f:
                    f.write(str(java_list))
                    f.close()
                with open(file='admin_list.txt', mode='w+',
                          encoding='utf-8') as f:
                    f.write(str(java_list))
                    f.close()
                with open(file='chat_gpt_list.txt', mode='w+',
                          encoding='utf-8') as f:
                    f.write(str(java_list))
                    f.close()
                with open(file='summon_images_list.txt', mode='w+',
                          encoding='utf-8') as f:
                    f.write(str(java_list))
                    f.close()
        return "root"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8899, debug=True, threaded=True)
