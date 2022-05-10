import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

def main():
    s = S()
    s.x = 1
    s.y = 2
    s.z = 3
    buf = ctypes.create_string_buffer(s, 3*s.x.size)

    print(buf.raw)
</code>
But it gives me this error:
<blockquote>
<p>TypeError: b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00' is not an integer</p>
</blockquote>
I'm not sure why I'm getting this error, but I'm pretty sure that the <code>buf</code> variable is not a string.
How can I fix this? Thanks in advance.


A:

<code>create_string_buffer</code> has nothing to do with structures. It creates a string buffer with a given length and initial value.
<code>buf = ctypes.create_
