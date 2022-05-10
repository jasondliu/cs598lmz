import lzma
# Test LZMADecompressor
dec = lzma.LZMADecompressor()
fp = open(r'F:\test\test.7z','rb')
header_data = fp.read(13)
header = struct.unpack('<BBBBIBBI',header_data)
magic,major,minor,start_header_crc,start_header_size,start_header_crc_is_valid,record_type,record_size = header
if magic != 0x5d:
    raise IOError('Not a 7z file.')
if record_type != 0xa3:
    raise IOError('Haven\'t found any header.')
enc_data = fp.read(record_size)
dec_data = dec.decompress(enc_data)
fp.close()

data.append(header)
data.append(dec_data)
