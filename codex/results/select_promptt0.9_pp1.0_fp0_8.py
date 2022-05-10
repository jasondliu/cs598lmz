import select
# Test select.select()

sock2 = socket.socket()

sock2.bind(('', 4002))
sock2.listen(5)

print 'server socket 2 listening on port 4002'

read_list = [sys.stdin, sock2]
while True:
    readable, writable, errored = select.select(read_list, [], [], 10)
    if sys.stdin in readable:
        data = sys.stdin.readline()
        print data
    if sock2 in readable:
        client, addr = sock2.accept()
        data = client.recv(1024)
        if not data:
            print 'client gone'
            continue
        print 'received from client:', data
