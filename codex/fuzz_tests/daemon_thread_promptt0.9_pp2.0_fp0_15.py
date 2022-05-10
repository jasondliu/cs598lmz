import threading
# Test threading daemon with Werkzeug 0.9.1.

from werkzeug import serving
from werkzeug.testapp import test_app

from httplib import HTTPSConnection
from base64 import b64encode
from urlparse import urlparse

from urllib import urlopen
import socket, ssl

from multiprocessing import Process


class DaemonThreadingTCPServer(ThreadingMixIn, TCPServer):
    pass


class DaemonUnixStreamServer(UnixStreamServer):
    daemon_threads = True


class RequestHandler(BaseHTTPRequestHandler):
    server_version = 'TestServer 0.1'

    def address_string(self):
        return '%s:%s' % self.client_address

    def do_GET(self):
        resp = self.handle_request()
        # self.finish() does not close the connection.
        self.finish()
        return resp

    def do_POST(self):
        length = int(self.headers['Content-Length'])
        resp = self.handle_request(body=self
