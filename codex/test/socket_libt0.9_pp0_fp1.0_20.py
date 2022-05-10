import socket
import datetime
import logging

logging.basicConfig(filename="logs.txt",level=logging.INFO, format='%(asctime)s-%(levelname)s-%(message)s')

now = datetime.datetime.now()
today = now.strftime("%d-%m-%Y %H:%M:%S")
logging.info("Starting Zabbix server at %s" % today)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 10051))
server_socket.listen(0)

client_socket, address = server_socket.accept()
logging.info("First connection from %s" % str(address))

data = b''

while True:
    new_data = client_socket.recv(1024)
    if not new_data:
        break
    data = data + new_data

client_socket.close()

