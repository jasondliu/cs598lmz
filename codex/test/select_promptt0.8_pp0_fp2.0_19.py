import select
# Test select.select is working with a pipe
b,a = os.pipe()
pipein = os.fdopen(a)
pipeout = os.fdopen(b,'w')
for i in range(10000):
    pipeout.write(str(i))
    pipeout.flush()
    r, w, e = select.select([pipein], [], [])
    if r:
        assert pipein.readline() == str(i) + '\n'
# Test select.select is working with a socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('', 0))
serv.listen(5)
asyncore.loop(0.001, False, None, 1)   # flush the channel
clisock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clisock.connect(serv.getsockname())
clisock.setblocking(0)
r, w, e = select.select([clisock], [clisock], [clisock])
