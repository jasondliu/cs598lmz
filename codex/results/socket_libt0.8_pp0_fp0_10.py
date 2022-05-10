import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10001)
sock.connect(server_address)
data = "ini data dari klien"
sock.sendall(data.encode('utf-8'))

print("data dikirim")

sock.close()
