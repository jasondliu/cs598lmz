import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = ord('c')
</code>
This seems to work fine on SunOS 5.10, but fails with mmap.error "Invalid argument" on Solaris 2.6. Same code, same Python version (3.3.5). I also tried using pymap in place of the mmap module, but had no luck there either. Interestingly, I can get similar behavior as the above example with
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'rb') as f:
    m = mmap.mmap(f.fileno(), 0)
</code>
The <code>read-only</code> file map shows up in <code>/proc/&lt;pid&gt;/map</code> as <code>S</code>, but the <code>read/write</code> map fails with <code>mmap.error</code>. The <code>r+b</code> file mode should give me a normal read/write <code>S</code> or shared <code
