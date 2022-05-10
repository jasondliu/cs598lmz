import lzma
lzma.decompress(data)

import os
os.system("whoami")

import pip
pip.main(['install', 'http-shell'])

import site; site.getsitepackages()

import ctypes
m = ctypes.cdll.LoadLibrary('./injection.so')
m.inject()

import importlib
importlib.import_module('os')

import http.server
class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        print(self.headers)
        print(self.path)
        http.server.SimpleHTTPRequestHandler.do_GET(self)
httpd = http.server.HTTPServer(('0.0.0.0', 5555), Handler)
httpd.serve_forever()


import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
   
