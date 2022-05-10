import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access = mmap.ACCESS_WRITE)
    m[0] = ord('2')
    m[2] = ord('3')
    print(m[0])
    print(m[2])
</code>
This prints <code>50</code> and <code>51</code>, which are the ASCII values for <code>2</code> and <code>3</code>. The third character isn't inserted; instead it overwrites character 1. Similarly, this
<code>m[-1] = ord('4')
</code>
inserts a <code>4</code> at the end of the file.
If instead of <code>mmap.ACCESS_WRITE</code> I use <code>mmap.ACCESS_READ</code> then I can't write to it, and the assignment of <code>ord('2')</code> to <code>m[0]</code> raises a PermissionError.
I'm guessing that this is correct behaviour and it's possible to initialize a file with particular byte sequences and insert new byte sequences at arbitrary offsets without changing the length of the mapped segment
