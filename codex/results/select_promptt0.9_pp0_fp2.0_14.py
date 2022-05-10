import select
# Test select.select() blocking behavior, when the file descriptors
# passed to select() are the same as the file descriptors returned by
# select().  When fds are the same, select() must block until timeout
# occurs, even if select() knows the fds are already readable.
#
# http://bugs.python.org/issue3237
try:
    r, w = os.pipe()
except AttributeError as e:
    raise NotImplementedError(e)
try:
    os.write(w, b'x')
    l = select.select([r], [], [], 1)
    if len(l[0]) == 1 and os.read(r, 1) == b'x':
        raise AssertionError('select.select() did not block')
except:
    os.close(r)
    os.close(w)
    raise
os.close(r)
os.close(w)
