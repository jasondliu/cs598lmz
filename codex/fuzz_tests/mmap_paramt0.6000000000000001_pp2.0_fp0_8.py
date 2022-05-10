import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = ord('2')

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = ord('3')
</code>
This ends up with the file containing the character <code>3</code>, as I would expect. However, if I change the second <code>with</code> statement to:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = ord('3')
    m.close()
</code>
the file instead contains the character <code>2</code>. I'm trying to understand why this is. I know that the mmap object is not actually closed until the <code>with</code> statement block is exited, but why does this matter? The file should be flushed and closed by the <code>with</code> statement, and so the file should be updated with the character <code>3</code>.


A:

<blockquote>
<p
