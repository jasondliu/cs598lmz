import socket
import threading

tLock = threading.Lock()
shutdown = False

def receving(name, sock):
    while not shutdown:
        try:
            tLock.acquire()
            while True:
                data, addr = sock.recvfrom(1024)
                print(str(data))
        except:
            pass
        finally:
            tLock.release()

host = '192.168.1.20'
port = 0
server = ('192.168.1.20',9090)

#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#s.bind((host,port))
#s.setblocking(0)

#rT = threading.Thread(target = receving, args=("RecvThread",s))
#rT.start()

#alias = input("Name: ")
message = input(">")
#while message != 'q':
#    if message != '':
#        s.sendto(bytes(alias+": "+message,"utf8"),server)
