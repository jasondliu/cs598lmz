import socket
import threading
import time
import sys

def scan(port):
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((host,port))
        s.close()
        print('[+] Port %d is open'%(port))
    except:
        pass


host=sys.argv[1]
port_begin=int(sys.argv[2])
port_end=int(sys.argv[3])

for port in range(port_begin,port_end):
    t=threading.Thread(target=scan,args=(port,))
    t.start()
    time.sleep(0.1)
