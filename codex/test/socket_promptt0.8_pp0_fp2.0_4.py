import socket
# Test socket.if_indextoname()
def main():
	i = socket.if_nametoindex('br0')
	name = socket.if_indextoname(i)
	print('i: %s, name: %s' % (i, name))


if __name__ == '__main__':
	main()
