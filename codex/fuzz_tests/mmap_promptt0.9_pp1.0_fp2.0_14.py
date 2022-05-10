import mmap
# Test mmap.mmap.find()
m = mmap.mmap (-1, 4)
m.write('test')
m.seek(0)
print m.find('test')  # Correctly prints 0
print 'test'.find(m)  # Should print 0, but instead raises TypeError
</code>
I would really like to be able to do something like 
<code>import os
if os.path.isfile(what.find(where)):
  # Do something
</code>


A:

You can convert the buffer to a string, since <code>mmap</code> objects have a <code>__getitem__</code> method:
<code>print ''.__getitem__(slice(*m.find('test'), None))
</code>
In newer versions of Python (3.5+), you could also use the <code>mmap</code>'s <code>cast</code> method:
<code>print m.cast('c').tobytes()
</code>

