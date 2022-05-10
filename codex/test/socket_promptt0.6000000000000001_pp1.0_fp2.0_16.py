import socket
# Test socket.if_indextoname

def if_indextoname(index):
    try:
        return socket.if_indextoname(index)
    except Exception as ex:
        return str(ex)


def test_if_indextoname():
    assert if_indextoname(0) == 'lo'
    assert if_indextoname(1) == 'eth0'
    assert if_indextoname(2) == 'eno1'
    assert if_indextoname(3) == 'eno2'
    assert if_indextoname(4) == 'eno3'
    assert if_indextoname(5) == 'eno4'
    assert if_indextoname(6) == 'eno5'
    assert if_indextoname(7) == 'eno6'
    assert if_indextoname(8) == 'eno7'
    assert if_indextoname(9) == 'eno8'

# Test socket.if_nameindex

