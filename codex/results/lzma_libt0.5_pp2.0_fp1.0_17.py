import lzma
lzma.open('a.lzma', mode='rb')
# Traceback (most recent call last):
#   File "&lt;stdin&gt;", line 1, in &lt;module&gt;
#   File "/usr/lib/python3.7/lzma.py", line 709, in open
#     raise RuntimeError("liblzma is required for lzma compression")
# RuntimeError: liblzma is required for lzma compression
</code>
I installed <code>lzma</code> library, but still getting the same error.
<code>sudo apt-get install liblzma-dev

import lzma
lzma.open('a.lzma', mode='rb')
# Traceback (most recent call last):
#   File "&lt;stdin&gt;", line 1, in &lt;module&gt;
#   File "/usr/lib/python3.7/lzma.py", line 709, in open
#     raise RuntimeError("liblzma is required for lzma compression")
#
