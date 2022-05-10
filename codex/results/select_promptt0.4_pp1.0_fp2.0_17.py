import select
# Test select.select()

import socket

def test_select():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 0))
    s.listen(5)
    s.setblocking(0)
    s2, addr = s.accept()
    s2.setblocking(0)
    s3, addr = s.accept()
    s3.setblocking(0)
    s4, addr = s.accept()
    s4.setblocking(0)
    s5, addr = s.accept()
    s5.setblocking(0)
    s6, addr = s.accept()
    s6.setblocking(0)
    s7, addr = s.accept()
    s7.setblocking(0)
    s8, addr = s.accept()
    s8.setblocking(0)
    s9, addr = s.accept()
    s9.setblocking(0)
    s10, addr = s.accept()
    s10.set
