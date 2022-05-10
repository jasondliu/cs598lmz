import codecs
codecs.register_error('strict', codecs.ignore_errors)

#------------------------------------------------------------------------------
def _get_encoding(filename):
    """
    Try to determine the encoding of a file.
    """
    try:
        # Open the file as binary data
        f = open(filename, 'rb')
        # We use a set to make sure we only try to decode each encoding once
        encodings = set()
        # We'll use the chardet library to guess the encoding
        import chardet
        # Read a small chunk of the file
        chunk = f.read(1024)
        # Detect the encoding of the chunk
        result = chardet.detect(chunk)
        # Add the encoding to the set
        encodings.add(result['encoding'])
        # Keep reading chunks until we have at least 3 encodings
        while len(encodings) < 3:
            # Read another chunk
            chunk = f.read(1024)
            # Detect the encoding of the chunk
            result = chardet.detect(chunk)
            # Add the encoding to the set

