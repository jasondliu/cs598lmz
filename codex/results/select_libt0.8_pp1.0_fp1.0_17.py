import select
import socket
import struct

import urllib3

import six
from six.moves import SimpleHTTPServer

from . import exceptions


class StreamingHttpResponse(object):

    def __init__(self, stream, status_code, reason=None, headers=None):
        self._stream = stream
        self._status_code = status_code
        self._reason = reason
        self._headers = headers or {}
        self._content_length = None
        self._content_type = None
        if self._status_code == 204:
            self._content_length = 0
        elif 'content-length' in self._headers:
            try:
                self._content_length = int(self._headers['content-length'])
            except (ValueError, TypeError):
                del self._headers['content-length']
        self._content_type = self._headers.get('content-type')

    @property
    def content(self):
        if self._content_length is None:
            return None
        elif self._content_length == 0:
            return
