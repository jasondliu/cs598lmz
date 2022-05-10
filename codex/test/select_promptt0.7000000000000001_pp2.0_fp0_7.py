import select
# Test select.select
# select.select 函数的参数和返回值，可以参考下面的函数注释
def select_test():
	import socket
	s = socket.socket()
	s.bind(('127.0.0.1',6666))
	s.listen(10)
	s.setblocking(False)
	epoll = select.epoll()
	epoll.register(s.fileno(),select.EPOLLIN | select.EPOLLET)
	connections = {}
	addresses = {}
