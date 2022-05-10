import lzma
lzma.LZMACompressor()
</code>
And then I get this error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/local/lib/python3.3/lzma.py", line 20, in __init__
    raise ValueError("Invalid format specification")
ValueError: Invalid format specification
</code>

