import bz2
bz2.decompress('BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

# decompress should also accept a compression level as its optional argument
bz2.decompress('BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084', 9)

# when bz2.BZ2Compressor is used as a context manager and an exception is raised inside the with statement, the context manager exits normally, calling the close() method
c = bz2.BZ2Compressor()
try:
    with c:
        raise RuntimeError
