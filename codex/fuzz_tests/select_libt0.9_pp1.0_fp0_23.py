import select
import time

# local
from proxy import Proxy, ProxyError, color

# verbosity
logger = logging.getLogger(__name__)

# compressors in the order they are tried
COMPRESSORS = [
    ("deflate", b"\x78\x9c"), # deflate
    ("gzip", b"\x1f\x8b"), # gzip
]

class CacheEntry(object):
    """Stores the response of a HTTP request"""

    def __init__(self, client_response):

        # headers (string dict)
        self.headers = {}
        headers = client_response.headers()
        for key in headers:
            self.headers[key] = headers[key]

        # buffers
        self.data = bytearray()
        self.send_data = bytearray()

        # response ready callbacks
        self.ready_callbacks = set()

    def add_data(self, data):
        self.data += data

    def add_compressed_data(self, data):
        """Adds compressed
