from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(MPS_SAMPLE_DATA)

with open("MPS.bz2", "rb") as f:
    decompressor = BZ2Decompressor()
    file_content = decompressor.decompress(f.read())
    file_content = file_content.decode("utf-8")
    print(file_content)
# byte encoded string
encoded_data = b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\xff\xff\xff\x00\x00\x00\x21\xf9\x04\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b'

# transform the byte encoded string into a byte array
bytes_array = bytearray(encoded_data)

