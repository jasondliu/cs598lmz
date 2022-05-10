from lzma import LZMADecompressor
LZMADecompressor().decompress(res)
</code>
But I am getting error.
<code>raise LZMAError("Input is not valid LZMA data")

lzma.LZMAError: Input is not valid LZMA data
</code>
Could anybody help me to understand this error?


A:

The data in the <code>response</code> object is usually binary data. In this case it is an LZMA stream, which is a form of compression.
The <code>lzma</code> module supports a few different formats and if you use the <code>LZMADecompressor</code> class directly, you need to pass in the raw compressed LZMA data. That is not what you have in the <code>response</code> object; that is the compressed data with a header in front of it.
Use the <code>requests.get()</code> function with the <code>stream=True</code> keyword argument (set to <code>True</code>) to accept the compressed LZMA stream directly:
<code>res = requests.get("https://api.blockchain
