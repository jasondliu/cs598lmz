import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write_byte(b'0')


# check that small changes are not identified as changes
with open('test', 'r+') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write_byte(b'1')

    # Ask the OS to update the metadata of the file.
    f.flush()

    if m.read() == b'0':
        print('No change detected')
    else:
        print('change detected')


# check that second update is not identified as change
with open('test', 'r+') as f:
    m = mmap.mmap(f.fileno(), 0)
