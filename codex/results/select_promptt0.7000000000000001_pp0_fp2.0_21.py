import select
# Test select.select
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(5)

inputs = [sock]
while True:
    rs, ws, es = select.select(inputs, [], [])
    for r in rs:
        if r is sock:
            conn, addr = r.accept()
            print('Got connection from', addr)
            inputs.append(conn)
        else:
            try:
                data = r.recv(1024)
                disconnected = not data
            except socket.error:
                disconnected = True
            
            if disconnected:
                print('disconnected', r.getpeername())
                inputs.remove(r)
            else:
                print(data)
