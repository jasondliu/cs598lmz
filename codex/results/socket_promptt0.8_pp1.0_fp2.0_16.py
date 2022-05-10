import socket
# Test socket.if_indextoname.
import socket
import sys
from test.test_support import run_unittest
from collections import namedtuple

TestFunction = namedtuple("TestFunction", "name arg_types")

class TestSocketInterfaceName(unittest.TestCase):

    Functions = [TestFunction('if_indextoname', (int,)),
                 TestFunction('if_nameindex', ()),
                 TestFunction('if_nametoindex', (str,)),
                 TestFunction('gethostbyaddr', (str,)),
                 TestFunction('gethostbyname', (str,)),
                 TestFunction('gethostbyname_ex', (str,)),
                 TestFunction('gethostname', ()),
                 TestFunction('gethostname', ()),
                 TestFunction('getprotobyname', (str,)),
                 TestFunction('getservbyname', (str, str)),
                 TestFunction('getservbyport', (int, str)),
                 TestFunction('getaddrinfo', (str, str)),
                 TestFunction('getaddrinfo', (str, str, str)),
                 TestFunction('getaddrinfo
