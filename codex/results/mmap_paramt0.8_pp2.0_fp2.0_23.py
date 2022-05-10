import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(),0)
    m.resize(2)
</code>
Question: 
Why do I get "Fatal Python error: Segmentation fault" in the last line?
Edit:
Error also when run with gdb with <code>gdb ./python</code> and <code>run -c 'with open("test", "r+b") as f: mmap.mmap(f.fileno(),0).resize(2)'</code>


A:

I'm guessing that there is an integer overflow somewhere which is causing the subsequent <code>mmap</code> call to fail.
You can see that in <code>test.c</code> the call to <code>mmap</code> includes <code>MAP_PRIVATE</code>:
<blockquote>
<pre><code>&lt;code&gt;  if (flags &amp;amp; MAP_ANONYMOUS) {
      /* ignore filesz, offset */
      m = mmap(addr, len, prot, flags | MAP_ANON, -1, 0);
  }
  else {
      /* ignore files
