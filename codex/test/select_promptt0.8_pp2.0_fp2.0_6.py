import select
# Test select.select and select.poll
import os,fcntl

def test_select():
    if not hasattr(select, "poll"):
        return
    
    # Urgh, can't create anonymous pipes on Windows.  So we use a
    # NamedPipe instead - requires using the pipe module manually.
    if sys.platform == "win32":
        import pipe
        reader, writer = pipe.Pipe()
        writer.write("hello world\n")
        writer.close()
        fd = reader.fileno()
    else:
        r, w = os.pipe()
        os.write(w, "hello world\n")
        os.close(w)
        fd = r

    p = select.poll()
    p.register(fd, select.POLLIN)
    
    l = []
    for f,event in p.poll():
        l.append((f,event))
        if len(l) == 1 and fd in map(lambda x: x[0], l):
            data = os.read(fd, 100)
