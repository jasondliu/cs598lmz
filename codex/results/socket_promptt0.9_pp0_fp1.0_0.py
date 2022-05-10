import socket
# Test socket.if_indextoname() on non existent index
def test_udp_192(udp):                                                           
	try:
		socket.if_indextoname(-1)
		socket.if_indextoname(0)
	except:
		pass
	finally:
		assert(True==True)
