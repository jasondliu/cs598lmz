import lzma
lzma.LZMAError: Cannot allocate memory
</code>
I know I am running out of memory, but I want to know if there is a way to tell lzma to use less memory?


A:

You can pass the dictionary size to the <code>LZMACompressor</code> constructor:
<code>compressor = lzma.LZMACompressor(dictionary=1 &lt;&lt; 20)
</code>
This sets the dictionary size to 1 MiB. The default is <code>2 ** 23</code> (8 MiB).

