import codecs
codecs.register_error('strict', codecs.ignore_errors)

from twisted.internet import reactor, protocol, defer, task
from twisted.protocols import basic
from twisted.python import log

from . import exceptions, protocol_pb2, common

class Protocol(basic.Int32StringReceiver):
    def __init__(self, host, port, user, password, database,
                 charset='utf8', ssl=False, use_unicode=True,
                 client_flag=0, cursorclass=None, init_command=None,
                 connect_timeout=None, read_timeout=None, write_timeout=None,
                 use_pure=False, charset_name=None, sql_mode=None,
                 **kwargs):

        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset
        self.ssl = ssl
        self.use_unicode = use_unicode
        self.client_flag = client_flag
        self.cursorclass
