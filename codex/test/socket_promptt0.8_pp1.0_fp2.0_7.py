import socket
# Test socket.if_indextoname()
# This test requires a working network connection, so is skipped
# if the network configuration is not enabled.
if "network" in config.subsystems:
	for i in range(4):
		try:
			name = socket.if_indextoname(i)
		except IOError:
			try:
				name = socket.if_indextoname(i)
			except IOError:
				name = None
