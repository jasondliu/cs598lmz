from bz2 import BZ2Decompressor
BZ2Decompressor()
</code>
The error is:
<code>AttributeError: 'module' object has no attribute 'BZ2Decompressor'
</code>
However, there are PIL for python 2.4, 2.5 and 2.6 which does not have this specific problem. I have tried to copy the module from all 3 versions and cannot get it to work. I have compiled my module and it worked.
I also use the following line: 
<code>from bz2 import decompress
</code>
and it does not show this error.

