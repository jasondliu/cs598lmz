import socket
# Test socket.if_indextoname()

def test_socket_if_indextoname():
    try:
        _ = socket.if_indextoname(1)
    except Exception as e:
        print("Error:", e)
        return False
    return True


if __name__ == '__main__':
    if not test_socket_if_indextoname():
        sys.exit(1)
