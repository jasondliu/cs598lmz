from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed_data)

# b'The quick brown fox jumps over the lazy dog.'
</code>
The documentation for the <code>lzma</code> module states:
<blockquote>
<p>The <code>&lt;code&gt;lzma&lt;/code&gt;</code> module provides support for <a href="https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Markov_chain_algorithm" rel="nofollow noreferrer">LZMA</a> compression. This format is a Lempel-Ziv coding (LZ77) with a 128-bit CRC.</p>
</blockquote>

