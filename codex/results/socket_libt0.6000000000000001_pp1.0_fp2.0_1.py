import socket
import sys
import json
import time
import urllib
import urllib2
import hashlib
import hmac
import base64

class BaiduYuyin():

    def __init__(self, appid, api_key, secret_key):
        self.appid = appid
        self.api_key = api_key
        self.secret_key = secret_key
        self.update = time.time()
        self.expire = 30
        self.token = ''
        self.cuid = hashlib.md5(self.get_mac_address()).hexdigest()
        self.url = "http://vop.baidu.com/server_api"

    def get_token(self):
        if time.time() - self.update < self.expire:
            return self.token
        params = {'grant_type': 'client_credentials',
                  'client_id': self.api_key,
                  'client_secret': self.secret_key}
        url = 'https://openapi.baidu
