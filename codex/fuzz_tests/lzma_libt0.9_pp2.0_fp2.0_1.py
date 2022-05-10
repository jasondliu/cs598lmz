import lzma
lzma.LZMAFile
</code>
This works fine under macOS, but it fails on Linux, with:
<code>AttributeError: module 'lzma' has no attribute 'LZMAFile'
</code>
Do I need a different version of Python? It's the same version that was installed by anaconda.
I found the implementation of LZMAFile, and both its docstring, and the file that invokes it, state:
<code># Skip LZMAFile on non-Windows. It's useless for us as is.
if sys.platform == 'win32':
    from .xz_lzma_impl import LZMAFile
else:
    from .lzma_impl import LZMAFile
</code>
So, it seems that lzma.LZMAFile would not be supported for Linux. But the Python docs seem to indicate that it is.
How do I get this to work under Linux?

