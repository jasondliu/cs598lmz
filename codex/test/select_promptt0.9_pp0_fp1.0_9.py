import select
# Test select.select on a pipe with a writer and reader
# with a timeout.
import time

r, w = os.pipe()
r = os.fdopen(r)
w = os.fdopen(w, 'w', 0)

start = time.time()
try:
    while 1:
        ready = select.select([r], [], [], 0.5)
        if ready:
            break
        assert time.time() - start < 10, "blocking forever?"
except KeyboardInterrupt:
    pass
finish = time.time() - start
