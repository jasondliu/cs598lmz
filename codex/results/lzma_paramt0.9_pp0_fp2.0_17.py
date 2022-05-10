from lzma import LZMADecompressor
LZMADecompressor()
</code>
Unable to make the module work, So I went to https://github.com/cloudflare/python-lzma after seeing https://pypi.org/project/pylzma/
But, I couldn't make sense out of the explanation
<blockquote>
<p><em>pylzma is a wrapper around the liblzma library that gives the ability to read
or write files in the LZMA compressed format.</em></p>
</blockquote>
Does it mean I will have to download the source of the library and compile it for Windows as a DLL file?
Am I missing something? 


A:

Looking at the LZMADecompressor interface, that decompressor is reading compressed data from a stream, not from a file. I doubt it's trying to open a file on its own. You need to provide it with data, the same way you'd give it the output of a subprocess:
<code>with open('pathtofile', 'rb') as f:
    # read the compressed data from the file, and feed it to the decompressor
    decompressor = L
