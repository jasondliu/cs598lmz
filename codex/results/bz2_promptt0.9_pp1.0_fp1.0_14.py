import bz2
# Test BZ2Decompressor
with bz2.open("sample2.bz2", "rb") as f:
    s = f.read()
# s has read the compressed file
</code>


A:

This is a bug in PyPy at least through 2.3.1, which doesn't expose the <code>BZ2File</code> class as documented. You'll get the same behavior on Python 2.7, CPython, or PyPy if you <code>import bz2</code> and <code>print(bz2.BZ2File)</code>:
<code>$ pypy-2.3.1
Python 2.7.2 (0806c948fca87fc6a48c6f5261d59e4af4b3faf4, Jun 13 2013, 00:39:56)
[PyPy 2.3.1 with GCC 4.2.1 Compatible Apple LLVM 4.2 (clang-425.0.27)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
&gt;&gt;
