import socket

import tornado.template
import tornado.web
import tornado.websocket
import tornado.ioloop
import tornado.gen

import websockets

from aiortc import RTCPeerConnection, RTCSessionDescription
from aiortc.contrib.signaling import add_signaling_arguments, create_signaling

from asyncio import subprocess

class RTCIndexPage(tornado.web.RequestHandler):
    def get(self):
        loader = tornado.template.Loader('/Users/jason/Documents/python_projects/SIGINT_V3/SIGINT_V3/html_static/')
        self.write(loader.load('index.html').generate())

class WebSocket(tornado.websocket.WebSocketHandler, websockets.WebSocketServerProtocol):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pc = None
        self.offer = None
        self.answer = None

