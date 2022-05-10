import socket
# Test socket.if_indextoname() etc. on FreeBSD.

from test import support

has_ifindextoname = hasattr(socket, 'if_indextoname')
has_ifnametoindex = hasattr(socket, 'if_nametoindex')
has_if_nameindex = hasattr(socket, 'if_nameindex')

if has_if_nameindex:
    # If if_nameindex() doesn't exist, it's pointless to perform tests.
    # This is true on Linux.
    import socket
    import os

    # We don't have to hold onto these.
    socket.if_nameindex()

    ifindextoname = socket.if_indextoname
    ifnametoindex = socket.if_nametoindex
    if_nameindex = socket.if_nameindex

    # Issue #19073: FreeBSD had a bug where if_indextoname() would
    # sometimes return None, when called with an index corresponding
    # to an interface that had been destroyed.
    # See https://bugs.freebsd.org/bugzilla/show_bug.cgi?id
