import io
# Test io.RawIOBase
r = io.RawIOBase()
r.isatty()
r.readable()
r.seekable()
r.writable()
r.fileno()
r.close()
r.closefd()
r.read()
r.readinto()
r.readinto1()
r.readall()
r.write()
# Test io.BufferedIOBase
b = io.BufferedIOBase()
b.read()
b.read1()
b.readinto()
b.readinto1()
b.write()
b.detach()
# Test io.BytesIO.
bi = io.BytesIO()
bi.getvalue()
# Test io.StringIO.
si = io.StringIO()
si.getvalue()
# Test io.BufferedReader.
br = io.BufferedReader(r)
br.read()
br.read1()
br.readinto()
br.readinto1()
br.peek()
# Test io.BufferedWriter.
bw = io.BufferedWriter(r)
bw.write()

