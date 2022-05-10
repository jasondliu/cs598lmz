import gc, weakref

from common import TestCase, setup_servers
from hashlib import md5
import cherrypy


class Root:
    def index(self):
        return "index"
    index.exposed = True

class ErrorHandlingTest(TestCase):

    def test_error_in_request_thread(self):
        # This will raise an "EarlyExitException" error, which is caught and
        # turned into a 500 error.
        self.getPage('/')
        self.assertBody('Internal Server Error')


class OutputTest(TestCase):

    def test_outputfilter(self):
        class Root(object):
            def index(self):
                raise cherrypy.InternalRedirect('filtertest')
            index.exposed = True
            
            @cherrypy.expose
            def filtertest(self, **params):
                cherrypy.response.headers['Content-Type'] = 'text/html'
                return """<html><head><title>foo</title></head><body>bar</body></html>"""
            
            @cherrypy.expose

