import select
# Test select.select()
# https://docs.python.org/2/library/select.html#select.select

sock = socket.socket()
sock.bind( ('', 5555) )

sock.listen(10)
