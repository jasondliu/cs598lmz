import weakref
from tornado import gen

from toredis import Reader
from toredis._compat import ipaddr, string_types, text_type
from toredis.connection import Connection
from toredis.exceptions import ConnectionError
from toredis.parser import parse_reply
from ..utils import RedisToredisTestCase, is_string


class Callback(object):
    def __init__(self, callback, **kwargs):
        self.callback = callback
        self.args = kwargs
        self.callback_invoked = False

    def __call__(self, *args, **kwargs):
        self.callback_invoked = True
        self.args.update(kwargs)
        self.callback(*args, **self.args)


class TestConnection(RedisToredisTestCase):
    def setUp(self):
        super(TestConnection, self).setUp()

    def tearDown(self):
        for client in self.clients:
            client.disconnect()
        super(TestConnection, self).tearDown()

    def test__
