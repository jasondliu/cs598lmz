import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte at a time
with open('../../data/alice.xz', 'rb') as input, \
     open('../../data/alice.txt', 'wb') as output:
    while True:
        chunk = input.read(1024)
        if not chunk:
            break
        result = decompressor.decompress(chunk)
        if result:
            output.write(result)
        if decompressor.eof:
            break

# Close the file
decompressor.flush()
 
# Print the decompressed data
with open('../../data/alice.txt', 'r') as f:
    print(f.read()[:100])

# <script.py> output:
#     Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, 'and what is
