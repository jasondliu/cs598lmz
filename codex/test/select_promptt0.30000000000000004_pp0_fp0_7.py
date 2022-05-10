import select
# Test select.select()

import sys
from socket import *

def main():
    if len(sys.argv) < 3:
        print("argv is error")
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)
    rlist = [s]
    wlist = []
    xlist = []
    while True:
        rs,ws,xs = select.select(rlist,wlist,xlist)
        for r in rs:
            if r is s:
                c,addr = r.accept()
                print("Connect from",addr)
                rlist.append(c)
            else:
                data = r.recv(1024)
                if not data:
                    rlist.remove(r)
                    r.close()
                    continue
                print
