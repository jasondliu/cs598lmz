import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = ord('2')
</code>
This ends up with a "TypeError: 'str' does not support the buffer interface".
But why?
I'm opening a file in binary mode, so when I read or write to it I should get/write bytes, right?
Instead of the <code>ord('2')</code> I also tried <code>b'2'</code> and <code>int(2)</code>.
What I actually want to do is write the content of a <code>array.array('B')</code> to the file (which is not possible with the normal <code>write</code> method of the file object).
I'm doing this to write a single byte to the file. I'd prefer if I could do this without the <code>mmap</code> module if possible, but it's not a big deal.


A:

The <code>mmap</code> module will, by default, create a byte-based map.  When you use a constant like <code>ord('2')</code>, it will be interpreted as a character and converted to a string.
