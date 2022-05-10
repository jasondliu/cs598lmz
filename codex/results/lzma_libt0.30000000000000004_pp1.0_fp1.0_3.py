import lzma
lzma.LZMAError:
  code = 1
  message = 'LZMA error: Corrupted input'
</code>
I'm using Python 3.6.3 on Windows 10.
I've tried installing the <code>lzma</code> module using pip, but I get the same error.
Any ideas?


A:

I had the same problem. I solved it by installing the lzma module with the following command:
<code>pip install pyliblzma
</code>

