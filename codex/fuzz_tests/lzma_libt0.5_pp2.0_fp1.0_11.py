import lzma
lzma.LZMAError:
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lzma.py", line 108, in __init__
    errno.EINVAL, "Compressed data invalid")
OSError: Compressed data invalid
</code>
I have tried to install the <code>pylzma</code> module but it does not work.
I am using Python 3.6 on a Mac.
Thank you for any help.


A:

I had the same issue and resolved it by installing the lzma module:
<code>sudo apt-get install xz-utils
</code>

