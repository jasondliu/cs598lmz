import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), length=1)
    m[0] = b'\0'
</code>
Running this code on a file of size 1023 bytes, I have seen <code>m[0]</code> set to <code>b'\x00'</code> (as expected, because the file was empty) and also incorrectly set to <code>b'0'</code> (should be <code>b'\0'</code>).
I realise that <code>bytes</code> objects are immutable and that the line <code>m[0] = b'\0'</code> does not necessarily do what I think it does.
But the thing is, the code does not always does what I think it does. Sometimes it does, sometimes it does not. This is more than just a bit weird.
I have tested this on Python 3.6, 3.7 and 3.8. Do other versions behave differently?

