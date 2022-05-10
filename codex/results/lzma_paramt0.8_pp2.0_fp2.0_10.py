from lzma import LZMADecompressor
LZMADecompressor.__module__ = 'lzma'

if sys.version_info < (3,):
    try:
        from cStringIO import StringIO
    except ImportError:
        from io import StringIO
else:
    from io import BytesIO


def decompress(source, xzpath='xz'):
    """
    Decompress a file object, returning a file object.

    :param file source: A file object that supports seeking and tell.
    :param str xzpath: Path to the xz executable.
    """
    source.seek(0)  # We read from the beginning of the file
    if not isinstance(source, StringIO):
        source = source.read()
    source = BytesIO(source)
    with NamedTemporaryFile() as tmp_source:
        tmp_source.write(source.read())
        tmp_source.seek(0)
        # This doesn't support the chunk size argument yet, but it doesn't
        # matter because we aren't doing streaming decompression.
        decompressor = BackportsLZMADecompressor()
