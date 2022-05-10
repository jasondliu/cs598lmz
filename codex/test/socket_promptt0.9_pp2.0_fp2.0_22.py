import socket
# Test socket.if_indextoname() on Linux, which is supported since Python 3.4.
# This test does not work on FreeBSD because it does not support IP aliasing.
# Skip this test when IPv6 is disabled.
try:
   socket.if_indextoname(socket.if_nametoindex('lo'))
except (AttributeError, OSError):
    pass
else:
    assert socket.gethostbyaddr('127.0.0.1') == ('localhost', [], ['127.0.0.1'])
    assert socket.gethostbyaddr('127.0.1.1') == ('ares2.local.net', [], ['127.0.1.1'])
    assert socket.gethostbyaddr('127.0.1.1', socket.AF_INET) == ('ares2.local.net', [], ['127.0.1.1'])
    if not is_android:
        assert socket.gethostbyaddr('127.0.0.1', socket.AF_INET6) == ('localhost', [], ['::1'])
        assert socket.gethost
