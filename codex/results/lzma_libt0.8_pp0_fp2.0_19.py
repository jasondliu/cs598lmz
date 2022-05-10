import lzma
lzma.LZMACompressor.compress(method=1, filters=[])
</code>
It gives the error:
<code>AttributeError: LZMACompressor instance has no attribute 'compress'
</code>
I found that link https://docs.python.org/3/library/lzma.html#lzma.LZMACompressor
I tried to use the same example but it throws the same error.
I am using Python 3.7 on Anaconda.


A:

The documentation of python on the page you linked is for version 3.7.1 (latest).
When I run the command <code>pip3 show lzma</code> on my computer,
I get this output:
<code>Name: lzma
Version: 0.4.8
Summary: Python binding for the LZMA compression library
Home-page: https://bitbucket.org/paul.moore/python-lzma/
Author: Paul Moore, Daniel Stutzbach, Per Ă…ngstrĂśm, Nathan Daly
Author-email: paul@
