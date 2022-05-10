import threading
# Test threading daemon mode
class DaemonThread(threading.Thread):
	def __init__(self, host, port, sock_type, tn_socket):
		threading.Thread.__init__(self)
		self.host = host
		self.port = port
		self.sock_type = sock_type
		self.tn_socket = tn_socket
		self.daemon = True
		self.start()
	def run(self):
		recv_data = self.tn_socket.read_until('\n',timeout=5).decode('utf-8')
		self.recv_data_queue.put(recv_data)
		print(self.name + ": " + recv_data)
		self.tn_socket.write(self.cmd.encode('utf-8'))
		self.tn_socket.write('\n')
	def set_cmd(self, cmd, recv_data_queue):
		self.cmd = cmd
		self.recv_data_queue
