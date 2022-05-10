import select
import sys
import signal

def signal_handler(signal, frame):
	print("\nprogram exiting gracefully")
	sys.exit(0)

def main():
	signal.signal(signal.SIGINT, signal_handler)
	if(len(sys.argv) < 2):
		print("Usage: " + sys.argv[0] + " <port>")
		sys.exit()
	port = int(sys.argv[1])
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server.bind(('', port))
	server.listen(5)
	inputs = [server]
	outputs = []
	message_queues = {}
	while inputs:
		readable, writable, exceptional = select.select(inputs, outputs, inputs)
