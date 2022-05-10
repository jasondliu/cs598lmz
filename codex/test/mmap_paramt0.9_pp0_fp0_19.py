import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = ord('a')
    m.close()


# output:
# b'a'

with open('test', 'r+b') as f:
    print ("-------------- test --------------")
    mmap.mmap(f.fileno(), 0)

    print ("-------------- test --------------")


#output:
# -------------- test --------------
# Traceback (most recent call last):
#   File "mmap3.py", line 15, in <module>
#     with open('test', 'r+b') as f:
#   File "/usr/lib/python3.5/codecs.py", line 321, in decode
#     (result, consumed) = self._buffer_decode(data, self.errors, final)
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0x61 in position 0: invalid start byte


with open('test', 'r+b') as f:
    print ("-------------- test --------------")
    mmap.mmap(f.fileno(), 1)
