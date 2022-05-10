import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    if_indextoname = socket.if_indextoname
    if_indextoname(1)
    if_indextoname(1, 'foo')
    try:
        if_indextoname(1, 'foo', 'bar')
    except TypeError:
        pass
    try:
        if_indextoname(1, 'foo', 'bar', 'baz')
    except TypeError:
        pass
    try:
        if_indextoname(1, 'foo', 'bar', 'baz', 'quux')
    except TypeError:
        pass
    try:
        if_indextoname(1, 'foo', 'bar', 'baz', 'quux', 'spam')
    except TypeError:
        pass
    try:
        if_indextoname(1, 'foo', 'bar', 'baz', 'quux', 'spam', 'eggs')
    except TypeError:
        pass
    try:
        if_indext
