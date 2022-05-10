from bz2 import BZ2Decompressor
BZ2Decompressor()

# Py2: ImportError: No module named bz2
# Py3: TypeError: start_bz2decompressor() missing 1 required positional argument: 'wbits'
</code>
What is causing the different behavior between Py2 and 3?


A:

While the <code>bz2</code> module will always be available and is responsible for the <code>BZ2Compressor</code> and <code>BZ2Decompressor</code> classes and the <code>compress</code> and <code>decompress</code> functions, the implementation of those things has been moved to C in the Python 3.3 C implementation (<code>python3.3-dbg/Modules/_bz2module.c</code>).
<code>BZ2Compressor()</code> and <code>BZ2Decompressor()</code> are now simply wrappers around <code>BZ2_bzCompressInit</code> and <code>BZ2_bzDecompressInit</code>.
The reason you used to be able to just instantiate the decompressor
