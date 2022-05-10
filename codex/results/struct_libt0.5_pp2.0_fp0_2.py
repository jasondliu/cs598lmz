import _struct

def convert(infile, outfile, in_format, out_format):
    """
    Convert a binary file from one format to another.
    """

    with open(infile, 'rb') as f:
        data = f.read()

    try:
        data = _struct.unpack(in_format, data)
    except Exception as e:
        raise Exception("Unable to unpack data using format {}: {}".format(in_format, e))

    try:
        data = _struct.pack(out_format, *data)
    except Exception as e:
        raise Exception("Unable to pack data using format {}: {}".format(out_format, e))

    with open(outfile, 'wb') as f:
        f.write(data)
