import select
# Test select.select()
#
# Set up two pipes and some stdin input.

r, w = os.pipe()
r2, w2 = os.pipe()

# make non-blocking
for fd in (r, r2):
    fl = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)

print('ready to read')

inputs = [r, r2, sys.stdin]

while True:
    # watch for inputs on all three inputs
    readable, writable, exceptional = select.select(inputs, [], [])
    print('select returned', readable, writable, exceptional)
    if not (readable or writable or exceptional):
        print('  timeout')
        continue

    for fd in readable:
        if fd is sys.stdin:
            s = fd.readline()
            print('stdin:', s)
        else:
            s =
