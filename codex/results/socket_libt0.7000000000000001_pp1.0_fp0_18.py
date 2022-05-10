import socket
import time

def udp_broadcast(host,port,msg):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
	s.sendto(msg, (host, port))
	time.sleep(0.5)
	s.close()

def udp_broadcast_array(host,port,array):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
	for i in array:
		s.sendto(i, (host, port))
		time.sleep(0.1)
	s.close()

def udp_broadcast_id(id,port,msg):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.setsockopt(
