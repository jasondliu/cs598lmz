import select
import time

# assume ipaddress is assigned IP address as per challenge
ipaddress = "127.0.0.1"
port = 3001

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((ipaddress, port))

# converse with server
while True:
    input = mysock.recv(500)
    if not input: break
    print(input.decode())
    if "goodbye" in input.decode(): break
    output = input.decode().replace(" ", "")
    mysock.sendall(output.encode())

mysock.close()
