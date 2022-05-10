import socket
import urllib.request
import urllib.error
import urllib.parse
import http.client
import re
import os
import sys
import json
import requests
import time
import hashlib

# 定义需要使用的全局变量
# 初始化headers
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
headers = {'User-Agent': user_agent}
# 使用百度AI开放平台的接口文档
# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_
