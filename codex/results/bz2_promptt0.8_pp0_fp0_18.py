import bz2
# Test BZ2Decompressor
def read_file(filename):
    with bz2.BZ2File(filename) as first_file, bz2.BZ2File(filename) as second_file:
        assert first_file.read() == second_file.read()

read_file('test.bz2')
</code>
And I get this error:
<code>Traceback (most recent call last):
  File "./read_file.py", line 10, in &lt;module&gt;
    read_file('test.bz2')
  File "./read_file.py", line 8, in read_file
    assert first_file.read() == second_file.read()
  File "/usr/lib64/python2.7/bz2.py", line 584, in read
    return self._buffer.read(size)
  File "/usr/lib64/python2.7/bz2.py", line 261, in read
    self._read()
  File "/usr/lib64/python2.7/bz2.py", line 279, in _
