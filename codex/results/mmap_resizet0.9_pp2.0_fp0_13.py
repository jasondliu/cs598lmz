import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The result is: <code>mmap.error: [Errno 9] Bad file descriptor</code>
After some research, I have red this answer, it explains why I get such error. It is also suggested to call <code>flush()</code> before truncate. But in this case, I get error <code>OSError: [Errno 109] Device or resource busy</code>
How can I truncate file that has mapped region ? I assume it should be possible because when I open the file in notepad, it allows to write and auto-saves changes.


A:

Just refer to the manual page:
<blockquote>
<p><code>&lt;code&gt;mmap.resize(new_size)&lt;/code&gt;</code></p>
<p>Resize the map, and create a new region at the end of the
resized map which is accessible for writing if <code>&lt;code&gt;mmap&lt;/code&gt;</code> was opened for
writing.</p>
<p>If <code>&lt
