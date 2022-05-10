import select

def main():
    s = socket.socket()
    s.bind(('0.0.0.0', 5000))
    s.listen(5)
    inputs = [s]
    while True:
        rs, ws, es = select.select(inputs, [], [])
        for r in rs:
            if r is s:
                c, addr = s.accept()
                print 'Got connection from ', addr
                inputs.append(c)
            else:
                try:
                    data = r.recv(1024)
                    disconnected = not data
                except socket.error:
                    disconnected = True
                if disconnected:
                    print r.getpeername(), 'disconnected'
                    inputs.remove(r)
                else:
                    print data

if __name__ == '__main__':
    main()
