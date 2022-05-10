import bz2
# Test BZ2Decompressor

def parse_bz2(file):
    """
    Parse BZ2 file
    :param file: BZ2 file
    :return: tuple of xml file and xml file text
    """

    bz_file = bz2.BZ2File(file)  # open the file
    xml_file = bz_file.read()  # get the decompressed data
    xml = xml_file.decode('utf-8')
    return xml_file, xml


def parse_bz2_streaming(file):
    """
    Parse BZ2 file
    :param file: BZ2 file
    :return: tuple of xml file and xml file text
    """
    xml_file = b""
    decompressor = bz2.BZ2Decompressor()
    with bz2.BZ2File(file) as f:
        for data in iter(lambda: f.read(100 * 1024), b""):
            xml_file += decompressor.decompress(data)

    xml = xml_file.decode('utf-8')
