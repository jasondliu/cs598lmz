import lzma
lzma.LZMAError("this")

def xtest_xz_stream():
    # This does not work yet as liblzma is not integrated into the
    # interpreter. Because of this, the module is not available in
    # a default installation.
    #
    # Unfortunately, this is not possible with the currently existing
    # liblzma C API, which is why we should wait until a new liblzma
    # C API has been written.

    # We don't want to depend on non-default modules.
    import lzma

    sio = io.BytesIO()
    xz = lzma.LZMACompressor()
    compressor = xz.compressobj()
    data = compressor.compress(b"x" * 1024)
    data += compressor.flush()
    sio.write(data)

    sio.seek(0)
    xz = lzma.LZMADecompressor()
    decompressor = xz.decompressobj()
    data = decompressor.decompress(b"x" * 1024
