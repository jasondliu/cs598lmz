import socket
# Test socket.if_indextoname()
port = 1234
ip = "0.0.0.0"
print socket.if_indextoname(1)

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)

serv_sock.bind((ip, port))
serv_sock.listen(1000)
sys.stdout.write("Listening ...")

def serve():
   while True:
     fd, addr = serv_sock.accept()
     while True:
       buff = fd.recv(4096)
       if not buff: break
       fd.send(buff)


for i in range(4):
   proc = Process(target=serve, args=(i,))
   proc.start()
