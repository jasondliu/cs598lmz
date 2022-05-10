import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)

    for i in range(10):
        m.write(str(i).encode())
        time.sleep(1)
        m.seek(0)
        print(m.readline())
