import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1, access=mmap.ACCESS_WRITE)
    print(m[:])
    print('A' in m)
</code>
It prints:
<code>b'\x01'
False
</code>


A:

<code>bytes(1)</code> - create a bytes sequence of length 1. This is a bytes object of length 1 whose one element is set to 0 (an integer).
<code>&gt;&gt;&gt; bytes(1)
b'\x00'
</code>
The letters <code>'A'</code> (or <code>'a'</code>, etc.) are used to create a bytes sequence. It calls <code>bytes.decode</code>:
<code>def decode(self, encoding="utf-8", errors="strict"): # known case of builtins.bytes.decode
    """Decode the bytes using the codec registered for encoding.
    encoding
      The encoding with which to decode the bytes.
    errors
      The error handling scheme to use for the handling of decoding errors.
      The default is 'strict
