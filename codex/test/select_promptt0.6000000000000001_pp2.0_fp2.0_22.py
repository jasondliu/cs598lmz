import select
# Test select.select()
def read_socks(socks):
	for sock in socks:
		data = sock.recv(1024)
