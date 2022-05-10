import mmap
import os
import re
import sys

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3


def get_version():
    version_py = os.path.join(os.path.dirname(__file__), 'sullivan', 'version.py')
    with open(version_py) as fp:
        version_file = fp.read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.groups()[0]
    raise RuntimeError("Unable to find version string.")


if PY2:
    from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

    class HTTPRequestHandler(BaseHTTPRequestHandler):
        def __init__(self, request, client_address, server):
            self.raw_requestline = request
            self.client_address = client_address
            self.server = server
