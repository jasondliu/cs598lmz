import codecs
# Test codecs.register_error - "surrogateescape" error handler

def check_surrogatepass(input, reader, writer, err="surrogateescape"):
    # input is a Unicode string
    # reader and writer are codecs
    # err is an optional error handler

    # Encode to byte string
    b = writer(input, err)

    # Decode back to Unicode string
    u = reader(b, err).decode(writer.encoding)

    # Check that we got back exactly the same string
    if u != input:
        raise AssertionError("%r != %r" % (u, input))

def check_surrogatepass_decode(input, reader, err="surrogateescape"):
    # input is a byte string
    # reader is a codec
    # err is an optional error handler

    # Decode to Unicode string
    u = reader(input, err).decode(reader.encoding)

    # Encode back to byte string
    b = u.encode(reader.encoding, err)

    # Check that we got back exactly the same string
