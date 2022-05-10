import ctypes
import ctypes.util
import threading
import sqlite3
import json
import subprocess
import signal
import os
import select
import sys
from pprint import pprint
from time import sleep
from http.server import HTTPServer, BaseHTTPRequestHandler
from queue import Queue


class MyHTTPServer(BaseHTTPRequestHandler):
    # default route
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(self.get_data())
    
    # accepts a post request and stores the data in a queue
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(length).decode('utf-8')
        
        data_queue.put(post_data)
        self.wfile.write(b'ok')
       
