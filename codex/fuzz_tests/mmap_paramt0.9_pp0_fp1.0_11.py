import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'
    m.flush()
    m.close()
</code>
And the other program:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    while True:
        if not m[0]:
            break
        time.sleep(10)
</code>
When the second program starts, I see the first program getting stuck forever at <code>m.flush()</code>
I also tried implementing the wait in the first program
<code>for i in range(10):
    print "Trying flush %d" % i
    try:
        m.flush()
    except PermissionError as e:
        time.sleep(1)
</code>
And here I'm stuck at <code>m.flush()</code> forever too.

