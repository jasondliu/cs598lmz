import _struct
# Test _struct.Struct("&gt;h") instance with bytes b'\x01\x00\x02\x00'
x = _struct.Struct("&gt;h")

expected = x.unpack_from(b'\x01\x00\x02\x00', 0)
got = x.unpack_from(b'\x01\x00\x02\x00', 0)
print(expected, got)
</code>
This code prints:
<code>(1, 2) (1, 2)
</code>
which is the expected output.
However, on Windows, it crashes with:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
WindowsError: exception: access violation reading 0x00000001
</code>
Python dev 3.6.8 from Python.org on Windows 10.
Minimal, self-contained example reproducing the crash:
<code>import _struct

def crash():
    x = _struct.Struct("&gt;h")
    expected = x
