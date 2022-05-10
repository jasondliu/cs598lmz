import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This results in the following traceback:
<code>Traceback (most recent call last):
  File "trunc.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: memory block is empty
</code>
I'd like to avoid closing and reopening the file as it seems to be looking for a valid region to mmap and that only gets set upon creating the file and truncating it.
I tried closing the file before truncating, then opening and truncating, which just results in the same error:
<code>Traceback (most recent call last):
  File "trunc.py", line 9, in &lt;module&gt;
    m = mmap.mmap(f.fileno(), 0)
ValueError: mmap length is zero
</code>


A:

If you are going to increase the size of the file, you'll need to first create a temporary file, write the data to the new file, mmap the new file, delete the original file and rename the new file back to the original name.
If you are not going to increase
