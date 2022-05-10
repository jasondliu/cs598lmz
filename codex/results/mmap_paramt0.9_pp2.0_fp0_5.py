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


def write_bytes(path, b):
    with open(path, 'wb') as f:
        f.write(b)

def read_bytes(path):
    with open(path, 'rb') as f:
        content = f.read()
    return content

if __name__ == '__main__':
    # path = 'test_log'
    # write_bytes(path, 'test')
    # append_str('\ntest1', path)
    # content = read_bytes(path)
    # print(content)
    with open('test', 'w') as f:
        f.write('test')
