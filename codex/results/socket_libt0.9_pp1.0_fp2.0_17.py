import socket
import sys

# Auslastung der CPU
def usage():
    return str(psutil.cpu_percent(interval=1))

host = '127.0.0.1' # localhost
port = 14000

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err_msg:
    print('Socket creation failed. Error code: ', str(err_msg[0]), ' , Error message : ', err_msg[1])
    sys.exit();

s.bind((host, port))
s.listen(10)

while True:

    conn, addr = s.accept() # akzeptieren von incoming connections

    print('Connected with ' + addr[0] + ':' + str(addr[1]))

    data = conn.recv(2048) # empfangen von Mitteilungen
    reply = 'OK...' + data

    if not data:
        break

    print("Client hat geschickt: " + str(data))
