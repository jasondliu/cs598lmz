import select
# Test select.select()

sock2 = socket.socket()

sock2.bind(('', 4002))
sock2.listen(5)
