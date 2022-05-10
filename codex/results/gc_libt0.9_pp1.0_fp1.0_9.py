import gc, weakref

class RequestHandler(HTTPServer.BaseHTTPRequestHandler):
    __slots__ = ['handle', 'client_address', 'headers', 'inbound', 'outbound',
                 'response_header_built', 'request', 'environ',
                 'response_code', 'outbound_headers', 'response_length',
                 'keep_alive', 'url_args', 'request_body', '_host']

    def setup(self):
        # PyPy fix: By default, PyPy removes extensions from __slots__.
        # This is unnecessary with our usage.
        self.__extend__ = ('handle', 'client_address', 'headers', 'inbound',
                           'outbound', 'response_header_built', 'request',
                           'environ', 'response_code', 'outbound_headers',
                           'response_length', 'keep_alive', 'url_args',
                           'request_body')
        HTTPServer.BaseHTTPRequestHandler.setup(self)
        self.outbound = []
        self.url_args = {}
        self.
