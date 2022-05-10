import select
# Test select.select()

sock = socket.socket()

sock.bind(('127.0.0.1', 50000))
sock.listen(5)

inputs = [sock]
outputs = []

while True:
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    
    for s in readable:
        if s is sock:
            conn, addr = s.accept()
            print('Connected')
            inputs.append(conn)
        else:
            data = s.recv(1024)
            if data:
                print(data.decode('utf8'))
            else:
                print('Disconnected')
                inputs.remove(s)
                s.close()
    
    for s in writable:
        pass
    
    for s in exceptional:
        print('Exception')
        inputs.remove(s)
        s.close()

sock.close()

# Test select.poll()

sock = socket.socket()

sock.bind(('127.0.0
