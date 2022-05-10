import ctypes
import ctypes.util
import threading
import sqlite3
import requests

from piwho import recognition
from tornado import gen
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application, url
from tornado.websocket import WebSocketHandler
from tornado.httpserver import HTTPServer
from tornado.process import Subprocess, SubprocessError


class HomeHandler(RequestHandler):

    def get(self):
        self.render("index.html")


class WSHandler(WebSocketHandler):
    waiters = set()
    waiters_lock = threading.Lock()

    def check_origin(self, origin):
        return True

    def open(self):
        WSHandler.waiters.add(self)
        print("New client connected")

    def on_close(self):
        WSHandler.waiters.remove(self)
        print("Closed client connection")

    @classmethod
    def broadcast(cls, msg):
        for waiter in cls.waiters:
            waiter.write_message(msg)

    def on_message(self, message):
        print("message received
