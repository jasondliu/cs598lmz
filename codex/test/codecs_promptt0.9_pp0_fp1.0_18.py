import codecs
# Test codecs.register_error("test.lookup", MyLookup("a").lookup)
# codecs.register_error("test.lookup3", Lookup3("a").lookup)
# codecs.register_error("test.lookup4", Lookup4("a").lookup)


def test_Search(cls, seekable):
    """Test the search functionality of the IncrementalDecoder class.

    cls is the class of the incremental decoder to use.
    seekable is the input file to use.
    """
    seekable.seek(0, 0)
    decoder = cls()
    while True:
        chunk = seekable.read(10000)
        if not chunk:
            break
        errors = (ord(c) for c in chunk)
        result, l, consumed, skip, offset = decoder.search(chunk, errors)
        if consumed != len(chunk):
            seekable.seek(-consumed + skip, 1)
        else:
            if decoder.last is None:
                decoder.nop()
