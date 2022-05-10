import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line (<code>m[:]</code>) raises a <code>ValueError</code>:
<code>ValueError: mmap offset is greater than file size
</code>
This is understandable, but I'm wondering if there's a way to make it work.
I tried to use <code>m.resize(0)</code> instead of <code>f.truncate()</code>, but that raises an exception:
<code>OSError: [Errno 22] Invalid argument
</code>
I also tried to use <code>m.resize(0, 1)</code>, but that didn't help either.
Is there a way to truncate the file and still access the memory mapped region?


A:

I think you can't do that.
When you create the memory map, you tell it the size of the file you want to map. If you change the size of the file, you have to update the size of the map.
You can do it by calling <code>m.resize(0)</code> after you truncate the file, but you won't be able to map the whole
