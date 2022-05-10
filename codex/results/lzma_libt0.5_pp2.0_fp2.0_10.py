import lzma
lzma.LZMAFile('test.xz')
</code>
This works fine on Linux, but I have trouble running it on Windows. I have installed pylzma according to the instructions on the website, but I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 4, in &lt;module&gt;
    lzma.LZMAFile('test.xz')
  File "C:\Python27\lib\site-packages\lzma.py", line 119, in __init__
    super(LZMAFile, self).__init__(fileobj, mode, format, filters)
  File "C:\Python27\lib\site-packages\lzma.py", line 89, in __init__
    self._init_decoder(filters)
  File "C:\Python27\lib\site-packages\lzma.py", line 94, in _init_decoder
    self._decoder = lzma_decoder(**kwargs)
  File "C:\Python27\lib\site-
