import io
# Test io.RawIOBase

# input
r = io.RawIOBase()
r.read()
r.read(1)
r.readinto()
r.readinto(b'')
r.readinto(b'', 1)
r.readall()
r.readline()
r.readlines()
r.readlines(1)
r.seek(1)
r.tell()
r.truncate()
r.truncate(1)
r.fileno()
r.isatty()
r.readable()
r.seekable()
r.writable()
r.write()
r.write(b'')
r.writelines()
r.writelines([b''])
r.close()
r.flush()
r.seekable()
r.readable()
r.writable()
r.name
r.closed

# output
w = io.RawIOBase()
w.write()
w.write(b'')
w.writelines()
w.writelines([b''])
w.seek(1)
w.tell()
w.tr
