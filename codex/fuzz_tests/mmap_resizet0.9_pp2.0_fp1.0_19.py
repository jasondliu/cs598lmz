import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
Looking at the mmap c api I can assume that having the file descriptor in the mmap object and closing the descriptor will avoid the problem. Is there a more pythonic way to remove the file descriptor from the mmap object?


A:

The following is a version of the OPs question code that works:
<code>import mmap

def main():
    with open('test', 'wb') as f:
        f.write(bytes(1))

    with open('test', 'r+b') as f:
        m = mmap.mmap(f.fileno(), 0)
        m[:] = b'12345678'
        print('m[:] =', m[:])
        f.truncate(5)
        m.resize(f.tell())
        # m should now be a valid mmap object, but it's all zeros
        print('after truncate m[:] =', m[:])


if __name__ == "__main__":
    main()
</code>
The key change is in <code>res
