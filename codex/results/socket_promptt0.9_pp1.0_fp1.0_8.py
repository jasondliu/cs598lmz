import socket
# Test socket.if_indextoname on Linux and Windows for IPv4 and IPv6
# (Python >= 2.6)


def if_indextoname_supported():
    return hasattr(socket, 'if_indextoname')


def test_error_message():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ok = is_linux or is_darwin or is_android
    try:
        name = socket.if_indextoname(10)
    except OSError as e:
        assert ok == (e.errno != errno.ENOSYS), \
            'if_indextoname failed: {}'.format(e)
    else:
        assert name == 'lo' or name == '\x00\x00\x00\x00\x00\x00\x00\x00\x00' +
                                    '\x00\x00\x00\x00\x00\x00\x01', \
                                    'unexpected name {}'.format(name)
