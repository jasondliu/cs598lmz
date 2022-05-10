import mmap

def read_in_chunks(fileName, chunk_size=512*1024*1024, max_size=10*1024*1024*1024):
    """
    Read a file in chunks of bytes
    Yields chunks of bytes of specified size

    fileName: File name to read
    chunk_size: Size of chunk to be read from file
    max_size: Maximum size to read from file
    """
    with open(fileName, "rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if chunk:
                yield chunk
            else:
                break


def read_in_blocks(fileName, block_size=512*1024*1024, max_size=10*1024*1024*1024):
    """
    Read a file in chunks of blocks
    Yields chunks of blocks of specified size

    fileName: File name to read
    block_size: Size of block to be read from file
    max_size: Maximum size to read from file
    """
