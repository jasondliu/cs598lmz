import socket
import sys
import threading

def connection(client_ip,client_port,send_to_server_queue,msg_to_send,chatlog):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((client_ip,client_port))
    print("Connection Established")
    while True:
        if not send_to_server_queue.empty():
            server.send(send_to_server_queue.get())
        else:
            time.sleep(0.1)
        msg_recived = server.recv(1024)
        if msg_recived == b'exit':
            print("server terminated")
            break
        #print(msg_recived.decode("utf-8"))
        if msg_recived != b'':
            chatlog.append(msg_recived)
    server.close()
