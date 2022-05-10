import threading
threading.stack_size(2*1024*1024)

def send():
    while True:
        info = input()
        clientsock.send(info.encode())

t=threading.Thread(target=send)
t.start()

while True:
    data = clientsock.recv(1024)
    print(data.decode())
