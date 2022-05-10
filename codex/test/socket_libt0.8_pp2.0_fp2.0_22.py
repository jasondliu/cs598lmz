import socket
from select import *

s = socket.socket()
s.bind(('', 1234))
s.listen(5)

# Подготовка для работы с множестом сокетов
rList = [s]
wList = []
xList = []

while True:
    (rs, ws, xs) = select(rList, wList, xList)

    for r in rs:
        if r is s:
            (conn, address) = s.accept()
            rList.append(conn)
        else: 
            data = r.recv(1024)
            if data:
                for w in wList:
                    w.send(data)
            else:
                rList.remove(r)
                wList.remove(r)

    for w in ws:
        wList.append(w)
