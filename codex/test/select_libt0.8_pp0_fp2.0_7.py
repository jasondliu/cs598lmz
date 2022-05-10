import select
import socket

logger = logging.getLogger('rpi_httpserver')

try:
    Server = BaseHTTPServer.HTTPServer
except AttributeError:
    Server = http.server.HTTPServer
try:
    BaseRequestHandler = BaseHTTPServer.BaseHTTPRequestHandler
except AttributeError:
    BaseRequestHandler = http.server.BaseHTTPRequestHandler

class HTTPRequestHandler(BaseRequestHandler):
    """
    The request handler for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def do_GET(self):
        """
        Serve a GET request.
        """
