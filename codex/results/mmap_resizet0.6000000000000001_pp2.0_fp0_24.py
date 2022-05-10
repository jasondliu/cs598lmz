import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This gives me a <code>ValueError: mmap offset is greater than file size</code>.
I tried to see if the file was closed, but both <code>f.closed</code> and <code>m.closed</code> are <code>False</code>.
I also tried to flush the file with <code>m.flush()</code> and <code>f.flush()</code>, but it did not help.
How can I truncate the file without getting this error?
Edit: I tried to use <code>os.ftruncate()</code>, and it works, but I cannot use it because the file is opened by the program I am trying to modify.
Edit: I am trying to modify a program that uses the <code>mmap</code> module, and I cannot change it. The program opens a file, then uses <code>mmap</code> and <code>truncate</code> on it. I want to modify the program so that it does not give a <code>ValueError</code>. My code should not use <code>mmap</code>, since it is not available in
