import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an "exceptional condition" (see the manual page for what your system considers such a condition)
# timeout: if not specified, wait forever

# Return value: three lists of objects that are ready

# Example:
# >>> import select
# >>> import socket
# >>> s = socket.socket()
# >>> s.connect(('www.sina.com.cn', 80))
# >>> s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# >>> s.recv(1024)
# b'HTTP/1.1 301 Moved Permanently\r\n'
# >>> select.select([s], [], [], 5)
# ([], [], [])
# >>> s.recv(1024)
# b'Server: nginx\r\n'
