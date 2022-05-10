import socket
# Test socket.if_indextoname with Interface name (Integer value)

def callback(name, result, err):
	print('Name: ' + name + ' , Result = ', result, ', Errno = ', err)

def test_socket_if_indextoname_with_name():
	result = socket.if_indextoname(13, callback)
	if result == None:
		print('Name Resolution Success')
	else:
		print('Name Resolution Failure')
	
if __name__ == "__main__":
	test_socket_if_indextoname_with_name()
