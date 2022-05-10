import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print(type(m))
print(m[:])
</code>
What it outputs is (on Linux x64):
<code>&lt;class 'mmap.mmap'&gt;
b''
</code>
The output of <code>repr(m[:])</code> is <code>b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'</code>.
What is <code>m[:]</code> referring to? Am I missing a step? Is there something I should be doing differently?
I tried looking at the source code, at mmapobject.c, and it looks like it's not supposed to return anything if the file has been truncated. Can anyone enlighten me on this behavior?


A:

If the file is truncated then your mmap object becomes invalid:
<blockquote>
<p>Upon initialization, the entire file is mapped into memory. This is
  usually more efficient than using Python’
