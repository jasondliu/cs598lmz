import select
# Test select.select()
# Address Family is AF_INET6
# socket.creatsock() -> socket.fromfd()
# socket.fromfd() -> socket.__new__() * calls af_inet6_socket()
# socket_dup() -> socket.fromfd()
# socket.fromfd() -> socket.__new__() * -> af_inet6_socket()
# test_unix_socket() -> socket.fromfd()
# socket.fromfd() -> socket.__new__() * -> af_unix_socket()
# test_id_type() -> socket.fromfd()
# socket.fromfd() -> socket.__new__() * -> any other type of socket
# call PyType_Ready then call PyObject_Init(sockobj, _PySocket_Type())
# test_makefile() -> (--implicit--) socket.makefile() *

import sys
import types
import unittest
from test import support, socket_helper
from test.support import import_module
from test.support.script_helper import assert_python_ok

