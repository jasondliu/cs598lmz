import select
# Test select.select()
from time import time, sleep
from socket import socket, AF_INET, SOCK_STREAM

def now():
    return time()

myHost = ''
myPort = 50007
if len(sys.argv) == 3:
    myHost, myPort = sys.argv[1:]
numPortSocks = 2

mainsocks, readsocks, writesocks = [], [], []
for i in range(numPortSocks):
    portsock = socket(AF_INET, SOCK_STREAM)
    portsock.bind((myHost, myPort))
    portsock.listen(5)
    mainsocks.append(portsock)
    readsocks.append(portsock)
    myPort += 1

print('select-server loop starting')
while True:
    readables, writeables, exceptions = select.select(readsocks, writesocks, [])
    for sockobj in readables:
        if sockobj in mainsocks:
            newsock, address = sockobj.accept()
