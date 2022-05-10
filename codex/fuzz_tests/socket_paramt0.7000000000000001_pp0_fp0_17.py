import socket
socket.if_indextoname(3)

# 获取指定网卡的ip地址
import netifaces as ni
ni.ifaddresses('eth0')
ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']

# 获取本机的ip地址
import socket
socket.gethostbyname(socket.gethostname())
"""

# 简单的服务器
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.
