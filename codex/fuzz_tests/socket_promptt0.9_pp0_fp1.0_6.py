import socket
# Test socket.if_indextoname


def test_if_indextoname(loop):

    name = socket.if_indextoname(1)

    if platform == 'win32':
        first_if = '\\Device\\NPF_{5EFF5DCD-18B5-4F4F-B497-28B229E310FA}'
        assert name == first_if


# Test socket.if_nameindex

def test_if_nameindex(loop):
    entries = socket.if_nameindex()

    if platform == 'win32':
        assert len(entries) > 0
        idx, first_if = entries[0]
        assert idx > 0
        assert first_if == '\\Device\\NPF_{5EFF5DCD-18B5-4F4F-B497-28B229E310FA}'


# Test socket.if_nameindex

def test_if_nameindex(loop):
    entries = socket.if_nameindex()

    if platform == 'win32':
        assert len(entries) > 0
        idx, first
