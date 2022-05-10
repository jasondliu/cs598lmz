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
        try:
            path = self.path.split('?')
            if path[0] == '/vol':
                vol = int(path[1])
                pi_radio.radio.set_volume(vol)
                self.response('OK')
            elif path[0] == '/url':
                if not pi_radio.radio.is_playing():
