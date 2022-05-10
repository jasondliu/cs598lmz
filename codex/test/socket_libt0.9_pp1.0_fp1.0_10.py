import socket
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('port', action='store', help='TCP port to connect to')

args = parser.parse_args()
print(args)
print(args.port)

#Get the hostname, IP Address from socket and set Port
#t_host = socket.gethostname()()
t_host = '192.168.4.73'
t_port = int(args.port)
#t_port = 7800
#t_ip = socket.gethostbyname(t_host)
