import socket
import sys

if len(sys.argv) < 3:
    print ("Please enter the ip and port of server to connect to.")
    print ("Usage: client.py [Ipv4] [Port]")
    sys.exit(1)

ip = str(sys.argv[1])
port = int(sys.argv[2])

print ("Attempting to connect to "+ip+":"+str(port))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip,port))

print ("Connected")

msg = str(' '.join(sys.argv[3:]))
msg = msg + '\r\n'

print ("Sending message: "+msg)

sock.send(msg)

print ("Closing socket")
sock.close()
print ("Disconnected")
