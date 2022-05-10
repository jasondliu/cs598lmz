import lzma
lzma.LZMAError: Not enough data for header
</code>
What am I missing?


A:

You are using LZMA library. From the docs:
<blockquote>
<p>This module provides a Python wrapper around LZMA compression library
  by Igor Pavlov.</p>
</blockquote>
The file you are trying to read is not a lzma archive.
You need to read it as a regular file like this:
<code>with open("test.7z","rb") as file:
  data = file.read()
</code>

