import select
# Test select.select() on a pipe.
r, w = os.pipe()

# test select() with a file descriptor that is >= FD_SETSIZE
import fcntl
fcntl.fcntl(r, fcntl.F_SETFL, os.O_NONBLOCK)
r = os.fdopen(r, 'rb', 0)
w = os.fdopen(w, 'wb', 0)

# Test select.select() on a pipe.

for i in range(5):
    print('pass')
    ready = select.select([r], [], [], 1)
    if ready[0]:
        print('ready')
        data = r.read(1)
        print('data', data)
        if not data:
            break
    else:
        print('sending')
        w.write(str(i).encode())
