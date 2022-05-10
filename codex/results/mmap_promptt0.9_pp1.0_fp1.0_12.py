import mmap
# Test mmap.mmap
<code> f = open('/mnt/ramdisk/testing', 'rb+')
 mm = mmap.mmap(f.fileno(), 0)
 mm.seek(0) 
 x = mm.readline()
 mm.seek(0) 
 mm.write(x+'111111') 
 mm.seek(0)
 mm.close()
</code>
w/o (mm.close()) and i get:
<code>mmap.mmap object at 0x7fa4b6c065a0
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
ValueError: I/O operation on closed file
</code>


A:

You get a ValueError without mm.close(). I presume that because your 'f' is closed and not shut electronically, a portion of the file is still buffered and not written. The garbage collector may also collect your 'f' if 'mm' is the last list referring to it. (There may be a 'close-by-mm' function in mm
