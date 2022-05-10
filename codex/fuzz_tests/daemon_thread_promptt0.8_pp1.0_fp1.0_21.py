import threading
# Test threading daemon
import time
# Test time
import random
# Test random
import multiprocessing
# Test multiprocessing


# Test create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Test bind socket
sock.bind(("127.0.0.1", 8888))
# Test listen socket
sock.listen(5)
# Test connect socket
sock.connect(("127.0.0.1", 8888))
# Test close socket
sock.close()
# Test buffer
buffer = "data"
# Test send data
sock.send(buffer)
# Test receive data
received = sock.recv(1024)
# Test get hostname
socket.gethostname()
# Test get host by name
socket.gethostbyname("localhost")
# Test get address info
socket.getaddrinfo("www.google.fr", None)
# Test get service by name
socket.getservbyname("ssh")
# Test get service by port
socket.getservbyport(22)
# Test get fq
