import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Test if_indextoname()
    if_indextoname = socket.if_indextoname
    if_indextoname(1)
    if_indextoname(1, 'foo')
    if_indextoname(1, 'foo', 'bar')
    if_indextoname(1, 'foo', 'bar', 'baz')
    if_indextoname(1, 'foo', 'bar', 'baz', 'quux')
    if_indextoname(1, 'foo', 'bar', 'baz', 'quux', 'spam')
    if_indextoname(1, 'foo', 'bar', 'baz', 'quux', 'spam', 'eggs')
    if_indextoname(1, 'foo', 'bar', 'baz', 'quux', 'spam', 'eggs', 'ham')
    if_indextoname(1, 'foo', 'bar', 'baz', 'quux', 'spam
