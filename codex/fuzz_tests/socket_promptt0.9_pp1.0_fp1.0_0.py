import socket
# Test socket.if_indextoname

def test_if_indextoname():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	indextoname = socket.if_indextoname(s.fileno())
	if (str(type(indextoname)) != "<type 'str'>"):
		return 'bad'
		
if __name__ == '__main__':
	print(test_if_indextoname())
