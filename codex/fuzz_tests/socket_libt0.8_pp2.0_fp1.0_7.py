import socket

BUFSIZE = 1024

cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cs.connect(("127.0.0.1", 1234))

while True:
    cmd = input(">>>")
    cs.send(cmd.encode())
    if not cmd:
        break
    server_msg = cs.recv(BUFSIZE)
    print(server_msg.decode())

cs.close()
