import select
import socket
import sys
import time
import traceback
import urllib
import urlparse

import tornado.httpserver
import tornado.ioloop
import tornado.iostream
import tornado.web

import sockjs.tornado

from sockjs.tornado import SockJSConnection

class EchoConnection(SockJSConnection):
    def on_open(self, info):
        print 'open'
        self.send('hello')

    def on_message(self, message):
        print 'message', message
        self.send(message)

    def on_close(self):
        print 'close'

if __name__ == '__main__':
    import logging
    logging.getLogger().setLevel(logging.DEBUG)

    EchoRouter = sockjs.tornado.SockJSRouter(EchoConnection, '/echo')

    app = tornado.web.Application(EchoRouter.urls)
    app.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
