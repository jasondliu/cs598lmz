import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0:1] = bytes(2)
    m.close()
</code>
On Windows, the above code works as expected. On Linux, I get the error:
<blockquote>
<p>mmap.error: [Errno 22] Invalid argument</p>
</blockquote>
I also tried writing to the file after opening it, but that didn't change anything. Does anyone know why this is?


A:

The problem is that you're opening the file with the <code>'b'</code> flag. In the documentation, it says:
<blockquote>
<p>The most commonly-used values of mode are 'r' for reading, 'w' for writing (truncating the file if it already exists), and 'a' for appending (which on some Unix systems means that all writes append to the end of the file regardless of the current seek position). If mode is omitted, it defaults to 'r'.</p>
</blockquote>
So in your case, it defaults to <code>'r'</code>. But <code>mmap</code> has this to say
