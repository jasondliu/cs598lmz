import select
# Test select.select()
# 
#
def accept_wrapper(sock):
	conn, addr = sock.accept()  # Should be ready to read
