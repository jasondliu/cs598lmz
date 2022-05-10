import mmap
# Test mmap.mmap vs StringIO.StringIO


def mmap_write(text):
    sIO = StringIO.StringIO(text)
    mm = mmap.mmap(sIO.fileno(), 0, access=mmap.ACCESS_WRITE)
    # Assume '\n' bounded lines
    mlines = text.split('\n')
    for l in mlines:
        mm.write("%s\n"...
</code>
Which will be more convenient and faster? I assume that the mmap is basically a fine-grained mmap to the file in this case. So what I mean by more convenient or faster is basically which one involves less hassle and has better performance.
Edit: As @syhpoon has pointed out, what I mean by fine-grained mmap is actually more appropriately called an anonymous mapping, rather than a true mmap file.

