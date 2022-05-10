import selectors

import sys
import time
from abc import ABC, abstractmethod
from enum import Enum


class HttpMethod(Enum):
    DELETE = object()
    GET = object()
    HEAD = object()
    PATCH = object()
    POST = object()
    PUT = object()


class HttpVersion(Enum):
    HTTP_1_0 = object()
    HTTP_1_1 = object()


class HttpRequest:
    def __init__(self, method, path, version, headers, body):
        self.method = method
        self.path = path
        self.version = version
        self.headers = headers
        self.body = body


class HttpResponse:
    def __init__(self, status, headers, body):
        self.status = status
        self.headers = headers
        self.body = body
        self.headers['Date'] = time.asctime(time.gmtime())
