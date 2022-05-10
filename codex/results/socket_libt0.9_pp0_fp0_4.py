import socket
import datetime
import time

server_host = '127.0.0.1'
port = 5000
client_socket = socket.socket()
client_socket.connect((server_host,port))

Mass = input("Please enter how much kg of  object :")
client_socket.send(Mass.encode())

time.sleep(1)

Speed = input("Please enter how much km/s :")
client_socket.send(Speed.encode())

time.sleep(1)

STR = input("Please enter how many STR or DEX or INT :")
client_socket.send(STR.encode())

time.sleep(3)

print(client_socket.recv(1024).decode())

client_socket.close()
