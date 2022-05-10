import socket

# fakes a connection to the server and sends a GET request
def send_request(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    sock.sendall(b"GET / HTTP/1.1\r\nHost: "+host.encode()+b"\r\n\r\n")
    return sock.recv(4096)

# get the server's IP address
host = socket.gethostbyname(socket.gethostname())
port = 8080

# print the response from the server
print(send_request(host, port).decode())
