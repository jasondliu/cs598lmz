import socket
import os
import threading

host = socket.gethostname()
port = 5000

s = socket.socket()
s.bind((host,port))

s.listen(5)

conn, addr = s.accept()

print(addr, "Has connected to the server")

name = 'C:\\Users\\User\\Desktop\\JAVA\\'

def RetreiveFile():
    filename = input(str("Please enter the filename: "))
    if os.path.isfile(name+filename):
        msg = "EXISTS"+str(os.path.getsize(name+filename))
        conn.send(msg.encode())
        userResponse = conn.recv(1024)
        if userResponse[:2] == 'OK':
            with open(name+filename, 'rb') as f:
                bytesToSend = f.read(1024)
                conn.send(bytesToSend)
                while bytesToSend != "":
                    bytesToSend = f.read(1024)
                    conn.send(bytesToSend)
   
