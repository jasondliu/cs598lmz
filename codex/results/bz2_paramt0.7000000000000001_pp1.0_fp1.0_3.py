from bz2 import BZ2Decompressor
BZ2Decompressor()
</code>
I'm getting an error which is:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/home/nuzhath/anaconda3/envs/tensorflow_p36/lib/python3.6/bz2.py", line 67, in __init__
    self.decompress = self._decompressor.decompress
  File "/home/nuzhath/anaconda3/envs/tensorflow_p36/lib/python3.6/bz2.py", line 17, in _decompressor
    self._decompressor = _bz2.decompressor()
TypeError: Required argument 'index' (pos 1) not found
</code>
What is the problem?


A:

Well, this is not a problem, this is a clear indication of a problem. 
<code>TypeError: Required argument 'index' (pos 1) not found
</code>
That's a pretty clear message
