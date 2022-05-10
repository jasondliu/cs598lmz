import selectors
import socket
import types
import os

# python3 sever.py


sel = selectors.DefaultSelector()
HOST = '127.0.0.1'
PORT = 65432
ENCODING = 'utf-8'


# 我们知道为了响应用户需求我们可能需要针对请求做不同的用户处理
# 如果用户请求我们需要在网页上显示一个字符串或者图片，那么我们就需要返回html文件串
# 或者对应的资源文件。所以我们需要判断
