import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[1:] = bytes(500)
</code>
I want to extend the file at offset 1, not the beginning. But this seems not to work. I thinks I've already understand why. When I create a mmap.mmap object, in order to get the content of the file, it loads the file firstly. The <code>bytes(1)</code> has only one byte, if I set the offset bigger than 1, then I get an <code>index out of range</code> error.


A:

I think you are writing off the end of the file. Your file starts as one byte long, so writing at offset <code>1</code> will write into byte position <code>1</code> and try to write five hundred more bytes including that, but the file only has one byte there and the next few hundred. So writing, say, five hundred bytes starting there is going to write into the same byte on the start <code>255</code> times, then into the next few hundred after that, which don't exist.
First, make the file five hundred and one bytes long with <code>bytes(501)</code> and
