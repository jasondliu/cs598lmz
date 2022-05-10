import lzma
# Test LZMADecompressor by decompressing a file created by LZMA
with lzma.open("data.xz", "rb") as f_in:
    # The read() method returns the empty bytes object at the end of the
    # compressed file, so we must check for that.
    data = f_in.read()
    if data == b'':
        print("The file is empty")
    else:
        print("The file has been decompressed successfully")

# Seek to the start of the file and decompress the entire file
# contents in one call.
with lzma.open("data.xz", "rb") as f_in:
    f_in.seek(0)
    data = f_in.read()
    print("The file has been decompressed successfully")
