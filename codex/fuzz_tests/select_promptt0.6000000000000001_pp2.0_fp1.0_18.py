import select
# Test select.select() on a pipe.
r, w = os.pipe()
r = os.fdopen(r)
w = os.fdopen(w, 'w')

for tout in (0, 1, 2):
    print('timeout =', tout)
    r.readline()
    if select.select([r], [], [], tout) == ([], [], []):
        print('  EOF')
    else:
        print('  data!')
    w.write('x')
    w.flush()


# Test select.select() on an AF_UNIX socket.
s = socket.socket(socket.AF_UNIX)
s.bind(support.TESTFN)
s.listen(1)

conn, addr = s.accept()
conn.setblocking(False)

for tout in (0, 1, 2):
    print('timeout =', tout)
    if select.select([conn], [], [], tout) == ([], [], []):
        print('  EOF')
    else:
        print('  data
