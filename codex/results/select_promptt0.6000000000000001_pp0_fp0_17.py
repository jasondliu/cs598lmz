import select
# Test select.select on all file descriptors in the range 0-1024.
# Should return empty lists.

for fd in range(1024):
    try:
        r, w, x = select.select([fd], [fd], [fd], 1.0)
    except ValueError:
        continue
    if r or w or x:
        print "select returned non-empty list for fd", fd
