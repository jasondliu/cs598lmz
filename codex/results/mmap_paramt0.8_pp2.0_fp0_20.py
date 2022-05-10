import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(1))
</code>
and I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 6, in &lt;module&gt;
    m = mmap.mmap(f.fileno(), 0)
ValueError: mmap length is zero
</code>
Why? How can I mmap a file of length 1?


A:

In your example, the file is opened with the <code>r</code> mode, which means read-only. It cannot be mmapped, because mmap would not be able to write to it. Change it to <code>'r+'</code>, or better yet, use <code>'rb+'</code>. 
The reason it works for your other example is that you are opening the file in the <code>'w+'</code> mode (write and read), which makes it writable.

