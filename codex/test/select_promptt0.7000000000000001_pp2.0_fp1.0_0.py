import select
# Test select.select
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setblocking(0)
s.bind(('127.0.0.1', 0))
s.listen(1)

port = s.getsockname()[1]

def client():
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect(('127.0.0.1', port))
    c.send(b'X')
    time.sleep(0.1)
    c.close()

threading.Thread(target=client).start()

r, w, e = select.select([s], [], [])
r[0].recv(1024)
r[0].close()

# Test select.poll
p = select.poll()
p.register(s, select.POLLIN)

