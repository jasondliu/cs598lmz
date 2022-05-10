import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[:] = b'\0'
    m.close()

def append_str(str, path):
    with open(path, 'a') as f:
        # f.write('\n%s' % str)
        f.write(str)
