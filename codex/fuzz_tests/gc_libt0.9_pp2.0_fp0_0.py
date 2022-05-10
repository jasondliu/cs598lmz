import gc, weakref

from urllib.parse import quote_plus, urlencode
from urllib.request import urlopen, Request

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)

def http_request(path, query = None, headers = None, payload = None, method = 'GET', username = None, password = None):
    path, query, headers, payload, method, username, password # unused
    raise NotImplementedError


def gen_descriptor():
    """
    This is a hack, but it's the only plausible way to extend a class with
    a property that has a unique ID, which is the only way to have a unique
    URL path for each object.
    """
    ID = 0
    while True:
        ID += 1
        yield property(lambda self: self.__dict__.setdefault('ID', ID))


class Resolver(object):

    """

