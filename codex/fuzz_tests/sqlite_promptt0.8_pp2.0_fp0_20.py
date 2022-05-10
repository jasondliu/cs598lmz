import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

import cherrypy
import cherrypy.lib.sessions
import cherrypy.lib.auth_digest
import cherrypy.lib.auth_basic

try:
    import win32api
except ImportError:
    win32api = None


session_lock = threading.Lock()


def setup_server():
    cherrypy.request.headers = cherrypy.lib.httputil.HeaderMap()
    cherrypy.response.headers = cherrypy.lib.httputil.HeaderMap()


def teardown_server():
    cherrypy.request.headers = None
    cherrypy.response.headers = None


def setup_session():
    cherrypy.session = cherrypy.lib.sessions.Session(id="abc",
                                                     lock=session_lock)
    cherrypy.session.acquire_lock()


def teardown_session():
    cherrypy.session.release_lock()
    cherrypy.session = None


class TestAuthDigest(helper.CPWebCase):
    setup_server = staticmethod(setup_
