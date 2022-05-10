from lzma import LZMADecompressor
LZMADecompressor().decompress(bytes)
</code>
Internet Explorer and Firefox both decompress it correctly, but Chrome complains that:
<code>* Error in decompressed stream: incorrect header check 
* Infile size (?, expected -1)
</code>
Here is a demo: http://ideone.com/8EyFoC
This demo compresses the same input with different ratios. If I use 3, I get no problem, with 4, the error in Chrome appears. This makes me suspect that something is wrong with the header, but the documentation I could find suggests that the header is supposed to be easily ignored.
Am I missing something?


A:

This looks like a bug in Chrome, but I'm not 100% sure.  The key is to try different values for <code>memlimit</code> in the <code>lzma.LZMACompressor</code> object creation.  For example, with <code>4</code> and <code>65536</code> Chrome failed to decompress my data, but <code>5</code> and <code>917504</code> (!) worked just fine.  Navigating to
