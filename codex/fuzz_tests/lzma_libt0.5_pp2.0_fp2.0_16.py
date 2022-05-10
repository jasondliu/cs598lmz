import lzma
lzma.open(file_path)
</code>
I get the following error:
<code>  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib/python3.5/lzma.py", line 246, in open
    return LZMAFile(filename, mode or 'r', **kwargs)
  File "/usr/lib/python3.5/lzma.py", line 73, in __init__
    self._open(mode, **kwargs)
  File "/usr/lib/python3.5/lzma.py", line 87, in _open
    self._buffer = io.BufferedReader(self._fileobj)
  File "/usr/lib/python3.5/io.py", line 1285, in __init__
    self.__init(raw, buffer_size)
  File "/usr/lib/python3.5/io.py", line 1305, in __init__
    self.raw.readinto(self._readbuf)
  File "/usr/lib/python
