import lzma
lzma.open(filename).read()
</code>
but this returns the same error.
Could it be that the file was not compressed with <code>lzma</code>? If so, how can I decompress this file?


A:

<code>lzma</code> module supports only .xz files, not .lzma.
Use <code>lzma.compress</code> and <code>lzma.decompress</code> to compress/decompress data in-memory.
You can use <code>lzma.LZMAFile</code> to read/write .xz files.
<code>lzma.LZMAStreamReader</code> is a wrapper for <code>lzma.LZMAFile</code>, which supports <code>io.BufferedIOBase</code> and <code>io.RawIOBase</code> interfaces. It can be used as a file-like object for <code>shutil.unpack_archive</code>.
<code>archive = lzma.LZMAFile(filename)
shutil.un
