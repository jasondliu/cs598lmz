import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]  # causes segmentation fault
</code>
Is there a way to make this work?
EDIT:
The use case for this is a file that is constantly being written to. I want to read the file, but do not want to read the same bytes twice. I also do not want to read the same bytes as a writer is writing.
I also want to avoid locking the file.
I'm fine with the solution being Linux/Mac specific. I'm just looking to make it work.


A:

The <code>mmap</code> object is no longer valid after the file is truncated.
You can use <code>m.close()</code> to clean up the <code>mmap</code> object, and then re-create the <code>mmap</code> object on the truncated file.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.close
