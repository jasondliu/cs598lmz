import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m[0] = b'\0'  # changing the value from 1 to 0
</code>
However, this is not working and the value is still 1.
Also, using <code>f.seek(0)</code> and <code>f.write(b'\0')</code> does not work.
What am I doing wrong?


A:

The <code>m[0] = b'\0'</code> is setting the first byte of the mapping to <code>b'\0'</code>, which is <code>00</code> (byte <code>0</code>); it's not unsetting the <code>0x01</code> that you wrote before.
You can use <code>m[:]</code> to get all the bytes in the mapping, and use <code>m[:] = b'\0'</code> to set all the bytes in the mapping to <code>b'\0'</code>.

