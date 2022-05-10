import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This gives:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 7, in &lt;module&gt;
ValueError: mmap cannot extend file
</code>
My question is - shouldn't <code>a</code> contain <code>b'\x01'</code>? I'd also be very interested in any reference to the documentation where I can clearly read that <code>m[:]</code> may not be valid anymore when the file gets truncated.
EDIT:
This looks to be a duplicate of Why do my mmap'ed blocks vanish if I truncate the file in Python?. The problem is in my code. I used 
<code>f.truncate()
a = m[:]
</code>
whereas <code>a = m[:]</code> should be before <code>f.truncate()</code>.


A:

<code>m[:]</code> is valid before <code>f.truncate()</code>, but isn't valid after that
