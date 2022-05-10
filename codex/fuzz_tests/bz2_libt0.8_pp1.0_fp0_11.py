import bz2
bz2.decompress(data)


def bz2_strings(data: bytes, min_length: int=20) -> Iterator[str]:
    """Return a list of decompressed bz2 strings of min_length from data."""
    length = min_length
    while length <= len(data):
        try:
            yield bz2.decompress(data[:length])
        except OSError:
            pass
        length += 1


def find_null_byte_strings(data):
    for i in range(len(data)):
        if data[i] == 0:
            yield data[:i]


def bytes_to_text(data: bytes) -> str:
    """Return data decoded as UTF-8 if valid, replacing errors with ? otherwise."""
    try:
        return data.decode('utf-8')
    except UnicodeDecodeError:
        return data.decode('utf-8', 'replace')


def find_bz2_strings(data: bytes, min_length: int=20) -> Iterator[str]:
