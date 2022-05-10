import select
# Test select.select

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 0))
sock.listen(5)

def run():
    r, w, x = select.select([sock], [], [], 0.2)
    print(r, w, x)

t = threading.Thread(target=run)
t.start()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(sock.getsockname())

t.join()
s.close()
