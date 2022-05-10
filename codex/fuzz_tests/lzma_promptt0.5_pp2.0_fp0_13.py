import lzma
# Test LZMADecompressor
decomp = lzma.LZMADecompressor()
# Read the entire file into a single byte string
with open('data.xz', 'rb') as f:
    file_content = f.read()
# Decompress the data
result = decomp.decompress(file_content)
# The output of the LZMA decompression is another XZ-compressed file
# We now decompress it using the XZ utils
result = subprocess.run(
    ['unxz', '--stdout', '--keep'],
    input=result,
    stdout=subprocess.PIPE,
    check=True,
)
print(result.stdout.decode('utf-8'))

"""
The LZMA module also contains a decompress() function that can decompress
data in one step. However, it does not support decompressing files that
contain multiple concatenated compressed streams.
"""
with open('data.xz', 'rb') as f:
    file_content = f.read()
result = lzma.decompress(file
