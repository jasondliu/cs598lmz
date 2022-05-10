from lzma import LZMADecompressor
LZMADecompressor = LZMADecompressor


def decompress(compressed):
    """Decompress a compressed data stream.

    :param compressed: bytes
    :return: bytes

    """
    decompressor = LZMADecompressor()
    return decompressor.decompress(compressed)


def decompress_file(compressed, output_file):
    """Decompress a file.

    :param compressed: bytes
    :param output_file: file
    :return: None

    """
    decompressor = LZMADecompressor()
    with open(compressed, 'rb') as input:
        with open(output_file, 'wb') as output:
            while True:
                chunk = input.read(65536)
                if not chunk:
                    break
                output.write(decompressor.decompress(chunk))


def compress(uncompressed):
    """Compress a data stream.

    :param uncompressed: bytes
    :return: bytes

    """
    compressor = LZMACompressor()
    return compressor.compress(
