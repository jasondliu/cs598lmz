import bz2
bz2.decompress(self.archive_object.read())
</code>
but the first four bytes of the uncompressed data are always <code>b'BZh'</code> which seems to be a header.
Is there a way to get the compressed data itself (and not the decompressed data)?


A:

Decompressing this data is a two stage process. 
The first stage is to inflate the data to some intermediate form - typically, the huffman codes present in the data are computed, and that's what you have stored in memory.
The second stage is to convert the intermediate form to the data itself. In this case, the intermediate form consists of huffman codes and they need to be used to expand the data to its original size.
If you want to change the data in the BZ2 archive, you need to find the intermediate data. 
For example, in the case of compressed text, that is easy to find. Just look for the <code>BZh</code> header. It's preceded by a <code>0x17 0x72 0x45 0x38 0x50 0x90</code> sequence.
