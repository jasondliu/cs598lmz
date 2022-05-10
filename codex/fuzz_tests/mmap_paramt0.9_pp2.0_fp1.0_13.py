import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[:] = bytes(2)

with open('test', 'rb') as f:
    print(f.read())
</code>
Unfortunately, this does not work in Python 3. In fact, Python raises a <code>OSError</code> with <code>[Error 12] Cannot allocate memory</code>. Is there any way to get around this issue?


A:

I recommend you check out the Value types section of the official Python documentation for mmap.
Here's what it says:
<blockquote>
<p>On POSIX, to map objects of other types, you must specify the
  <code>&lt;code&gt;mmap.MAP_SHARED&lt;/code&gt;</code> flag, and create an instance of the other type before
  mapping. For example:</p>
<pre><code>&lt;code&gt;m = mmap.mmap(f.fileno(), 0)
a = array.array('i', [0])
# size is always a multiple of the PAGESIZE (see os.getpagesize())
assert a
