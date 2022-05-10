import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
From what I understand, the mmap should be invalidated after the truncate call. And it does, if I try to access the memory map before closing it, I get an exception.
What I don't understand is, why I can still access the memory map after closing it, even though it was modified? 
I read the mmap documentation and it says:
<blockquote>
<p>Modifications to the mmap object or the file it is based on, will be
  visible through the other. However, there are a few notable exceptions.
  <strong>If the file on disk is truncated, modifications to the mmap object will no longer be reflected in the file</strong> (and vice versa).</p>
</blockquote>
I assume this is why an exception is raised when I try to access the memory map before closing it. But if this is the case, shouldn't I not be able to access the memory map after closing it? I don't understand why the memory map is still accessible. Could someone explain this?


A:

I found the answer in the documentation:
<blockquote>
<
