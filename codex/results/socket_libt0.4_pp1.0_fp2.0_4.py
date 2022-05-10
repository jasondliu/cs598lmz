import socket
import threading
import sys

def send_message(sock):
    while True:
        sendData = input('>>>')
        sock.send(sendData.encode('utf-8'))

def recv_message(sock):
    while True:
        recvData = sock.recv(1024)
        print('상대방 :', recvData.decode('utf-8'))

port = 8081

serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSock.bind(('', port))
serverSock.listen(1)

print('%d번 포트로 접속 대기중...'%port)

connectionSock, addr = serverSock.accept()

print(str(addr),'에서 접속되었습니다.')

sender = threading.Thread(
