import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
here, it will raise exception <code>mmap.error: [Errno 22] Invalid argument</code> at <code>a = m[:]</code>
but if move the <code>truncate</code> like this:
<code>with open('test', 'r+b') as f:
    f.truncate()
    m = mmap.mmap(f.fileno(), 0)
    a = m[:]
</code>
will work fine
so i tried to reproduce the problem using a <code>c</code> program, but it seems no problem, the code is very easy:
test.c
<code>#include &lt;stdlib.h&gt;

int main(int argc, char *argv[])
{
    char *p = NULL;
    munmap(p, 0);
    return 0;
}
</code>
and it will work fine, how ever with this python code, it raises exception as said in above.
so my question is, is there somewhere i have done wrong, or is there somewhere i have misunderstood?
