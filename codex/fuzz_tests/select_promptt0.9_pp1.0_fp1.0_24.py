import select
# Test select.select
print('Select-IO test')
while True:
    rlist, wlist, elist = select.select([sys.stdin,], [], [])
    if sys.stdin in rlist:
        input = sys.stdin.readline()
        print(input)
    else:
        print('Timeout...')


__author__ = 'liuhui'
import socket
s=socket.socket(socket.AF_UNIX,socket.SOCK_STREAM)
s.bind(\"./yong.sock\")
s.listen(1)
conn, addr=s.accept()
for i in range(1,5):
    print(conn.recv(1024))
    conn.send(bytes(\'hello %d\',str(i),'utf8'))
conn.close()
s.close()
