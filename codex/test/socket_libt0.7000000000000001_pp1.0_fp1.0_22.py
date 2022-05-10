import socket
import json

listeners = []

def send_message(msg):
	json_msg = json.dumps(msg)
	for listener in listeners:
		listener.send(json_msg)

def on_start():
	global sock
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = ('localhost', 9999)
	print >>sys.stderr, 'starting up on %s port %s' % server_address
	sock.bind(server_address)

	sock.listen(1)

def on_stop():
	sock.close()

def on_connect(connection, address):
	print >>sys.stderr, 'new connection from', address
	connection.settimeout(100)
	listeners.append(connection)

def on_disconnect(connection):
	print >>sys.stderr, 'connection lost'
	listeners.remove(connection)

def on_request(connection, address):
	print >>sys.stderr,
