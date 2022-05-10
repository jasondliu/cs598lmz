import socketserver
from logger import Logger
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import json
from PyQt5 import QtCore
from keymaster import KeyMaster
import threading
from time import sleep

class MyHandler(BaseHTTPRequestHandler):    
    def _set_response(self):
        self.send_response(200)
        sel
