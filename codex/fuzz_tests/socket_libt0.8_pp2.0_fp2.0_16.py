import socket
from urllib.parse import quote_plus, unquote_plus


class Server:
    def __init__(self, host, port, verbose=False):
        self.host = host
        self.port = port
        self.verbose = verbose

    def log(self, s):
        if self.verbose:
            print(s)

    def decode_request(self, request):
        self.log("Request str: %s" % request)
        request_lines = request.split(b"\r\n")
        command = request_lines[0]
        headers = {}
        first_line_tokens = command.split(b" ")
        headers["method"] = first_line_tokens[0]
        headers["url"] = first_line_tokens[1]
        headers["version"] = first_line_tokens[2]

        for header in request_lines[1:]:
            if header == b"":
                break
            header_name, header_value = header.split(b": ")
           
