from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open("sample.bz2").read())
</code>
But in the official Python documentation it doesn't have any decompress method for the BZ2Decompressor class. But there is a decompress method for the BZ2File class. 
So which one should I use?


A:

The <code>bz2</code> module is cross-version compatible in that the API is mostly the same. 
In Python 3.x the <code>BZ2Decompressor</code> class has a <code>decompress</code> method, but in Python 2.x it doesn't. In Python 2.x the <code>BZ2File</code> class did have the <code>decompress</code> method, but it no longer exists in either Python 3.x or 2.x.
However, by using the <code>BZ2File</code> class in both Python 2.x and 3.x you can get the same result (in both Python 2.x and 3.x):
<code>from __future__ import print_function
import bz2

with b
