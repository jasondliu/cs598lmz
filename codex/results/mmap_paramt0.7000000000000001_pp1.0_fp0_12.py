import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(5))
    m.seek(0)
    print(m.read(1))
    m.close()
</code>
I would expect that this code would print <code>5</code>, but it actually prints <code>1</code>. However, if I remove the first <code>mmap.mmap</code> call, it prints <code>5</code> as expected. 
Why is this happening?


A:

In the docs you can find this:
<blockquote>
<p>If the file is opened for read-only access, this is the same as
  accessing a regular file. If the file was opened for read and write
  access, this is the same as accessing a regular file in read and write
  mode. If the file was opened for write-only access, the file is
  <strong>created if it does not exist</strong>; otherwise it is treated as a regular
  file.</p>
</blockquote>
You are opening the file in <code>wb</code> mode, but the second time you open it in <code>
