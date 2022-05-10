import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()

print(a)
</code>
This prints <code>b'\x01'</code> on Linux, but <code>b''</code> on Windows. 
Why does this happen?


A:

The documentation for <code>mmap</code> says:
<blockquote>
<p>If <code>&lt;code&gt;mmap()&lt;/code&gt;</code> is used to map a file <em>into memory</em>, changes to the file will be visible in the memory map, and changes to the memory map will be written to the file.</p>
</blockquote>
The key here is that the file is mapped into memory; it doesn't necessarily stay in memory.
The reason you're seeing different behavior on Linux and Windows is that the <code>mmap</code> module uses different methods to map the file. On Linux, it uses the <code>mmap</code> system call, which is a direct mapping of the file; it doesn't stay in memory after the file is closed. On Windows, it uses <code>CreateFileMapping</
