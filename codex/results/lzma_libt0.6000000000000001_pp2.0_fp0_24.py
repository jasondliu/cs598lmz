import lzma
lzma.LZMACompressor

def process_file(filename, out_dir):
    if filename.endswith(".xz"):
        with lzma.open(filename, "rb") as f:
            data = f.read()
    else:
        with open(filename, "rb") as f:
            data = f.read()
    return process_data(data, out_dir)

def process_data(data, out_dir):
    # read the header
    header = data[:32]
    (
        magic,
        version,
        header_size,
        file_size,
        block_size,
        block_count,
        block_table_offset,
        block_table_length,
        meta_block_count,
        meta_block_offset,
        meta_block_length,
        checksum_type,
    ) = struct.unpack(">4sIIIIIIIIIIB", header)
    assert magic == b"\xfd7zXZ\0"
    assert version == 0x0001
   
