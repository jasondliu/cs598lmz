import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.seek(0)
    m.write(b'0')
    m.close()

with open('test', 'rb') as f:
    print(f.read())
</code>
The output is <code>b'0'</code>.
Now, I would like to change the code so that the <code>mmap</code> is not closed and the file is not closed by the script.
I've tried:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.seek(0)
    m.write(b'0')

print(os.stat('test').st_size)
</code>
The output is <code>1</code>, instead of <code>0</code>.
And:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.seek(0)

m.close()
m.write(b'0')
m
