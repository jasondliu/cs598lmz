import bz2
bz2.decompress(zlib.decompress(pickle.loads(data)))
</code>
I'm still working on the issue of the CRC. 

