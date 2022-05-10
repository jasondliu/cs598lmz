import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m)
    # Traceback (most recent call last):
    #   File ".\a.py", line 10, in <module>
    #     m.write_byte(b'A')
    # ValueError: invalid character
    m.write_byte(b'A')
