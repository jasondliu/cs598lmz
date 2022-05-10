import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    for i in range(st.st_size):
        print(m[i])
</code>
The output was as expected, 1.
But, when I make a change to the .txt file (save and refresh), the output from the same code is returns a <code>[83, 84, 32, 75, 111, 110, 115, 116, 32, 84]</code>. This is when the <code>print(m[i])</code> is changed to <code>print(m.readline())</code>.
Why is it that when I change the file and re-execute, it returns a string?
<code>m.read(2)</code> gives me <code>ST</code>.
<code>m.read()</code> prints out the whole file.
Is it possible to get 1, even if the file has been changed?
Thanks!


A:

My guess is that you're on Windows and your file encoding is UTF-16.
According to the documentation for R, <code>mmap</code> maps the file into the file's programming address space in "binary" mode, meaning, on
