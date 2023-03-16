# -*- coding: utf-8 -*-
from flask import Flask, request
import requests as req

app = Flask(__name__)


@app.route("/", methods=["post"])
def get_json():
    # 接收消息
    request_get_json = request.get_json()
    print(request_get_json)
    '''
    发消息
    req.get('http://127.0.0.1:5700/send_group_msg?group_id={}&message={}'.format(group, message))
    '''
    return "root"


if __name__ == '__main__':
    app.run("0.0.0.0", port=8899)
