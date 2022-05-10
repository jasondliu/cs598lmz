import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    m.close()
</code>
This prints <code>b'\x01'</code>, which is the old content of the file.
If instead of truncating I write to the file, then the content of <code>m</code> is updated.
I have read the documentation about <code>mmap</code> and searched for answers but I found nothing about this.
I'm using Python 3.8.3 on Windows 10.
I would like to know if this is a bug or expected behaviour. If expected, I would like to know why this happens and how can I avoid it.

