import bz2
bz2.BZ2Compressor()
</code>
The traceback is as follows:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/local/lib/python3.4/bz2.py", line 119, in __init__
    raise RuntimeError("bz2 extension not available.")
RuntimeError: bz2 extension not available.
</code>
I have tried installing bz2-devel, but that doesn't seem to have done anything.  Is there a way to make the bz2 library available to my user?  It's the only thing that seems to be missing.


A:

I had the same problem and solved it with installing bz2 with pip3:
<code>pip3 install bz2file
</code>

