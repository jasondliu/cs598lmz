import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
In this example the application raises <code>mmap.error: cannot truncate a mapped file</code> on line <code>f.truncate()</code>. I understand that I have to unmap the region before I can truncate but that would imply that I have to unmap the complete region, wouldn't it?
I have tried to use <code>m.resize(0)</code> but that doesn't seem to work after the file has been truncated. I have also tried to use <code>m.remap(0)</code> but that doesn't seem to work either when I afterwards try to map the region. Of course I could try to unmap the whole region and afterwards map everything again, but that is pretty much the same as unmap+truncate and I really don't want to do that. 
For the application I am working on I need to be able to truncate the file in case some error occurred. Is there no other way to truncate the file than unmapping it?


A:

<blockquote>
<p>I understand that I have to unmap the region before I can truncate but that would
