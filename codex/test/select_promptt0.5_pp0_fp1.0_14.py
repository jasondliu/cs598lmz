import select
# Test select.select()

def test_select():
    import select
    import socket
    import time
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("localhost", 80))
