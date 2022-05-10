import select
# Test select.select() with large number of fds and nonzero timeout.
# On Linux, this used to be very slow before Python 1.5.2.

SECONDS = 1
if len(sys.argv) > 1:
    SECONDS = int(sys.argv[1])

count = 1000
if len(sys.argv) > 2:
    count = int(sys.argv[2])

fds = []

for i in range(count):
    fds.append(os.open(support.TESTFN, os.O_RDONLY))

t1 = time.time()
r, w, x = select.select(fds, [], [], SECONDS)
t2 = time.time()

for fd in fds:
    os.close(fd)

print("select waited %.3f seconds; we expected to wait %d seconds" %
      (t2 - t1, SECONDS))
