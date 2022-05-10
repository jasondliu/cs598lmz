from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# This works in Python3, but not in Python2.
data.decode('utf-8')

# This works in Python2, but not in Python3.
unicode(data)
</code>
The <code>decode</code> method works in Python 3. In Python 2, strings are not Unicode by default. The <code>unicode</code> method works on <code>bytes</code> in Python 2, but not in Python 3.

