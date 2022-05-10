import socket
import threading

IP = '127.0.0.1'
PORT = 8081

sc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sc.connect((IP,PORT))

#action = input("Action: ")
#sc.send(action.encode())

while(True):

    action = input("Action (send,recv,exit): ")
    sc.send(action.encode())

    if(action == 'send'):
        text = input("Text: ")
        sc.send(text.encode())
    elif(action == 'recv'):
        print(sc.recv(100))
    elif(action == 'exit'):
        print("Exiting")
        sc.close()
        break

