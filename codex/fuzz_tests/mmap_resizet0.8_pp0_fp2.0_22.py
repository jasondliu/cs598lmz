import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:] # Segmentation fault
    m.close()
</code>

<code>$ python3 bug.py                                                                                                                                                                                                                                                           
Segmentation fault (core dumped)       
</code>


A:

Well, I have found the problem. Turns out, I forgot to <code>m.resize</code> after <code>ftruncate</code>.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.resize(0)
    try:
        a = m[:] # Segmentation fault
    except ValueError:
        print('Expected error') # We get here!
    m.close()
</code>

