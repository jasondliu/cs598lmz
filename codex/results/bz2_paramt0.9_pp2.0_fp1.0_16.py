from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz_compressed)

# Test print to terminal
# print('BZ2 Decompressed',bz_decompressed)



"""
Task 3.2 - Slightly more complex example using HTTP data
"""

# Load from URL using urllib
req = requests.get("http://www.pythonhow.com")
content = req.text

# Print some details
print('Content type:', type(content))
print('Content length:', len(content))

# Print the content
# print('Content:\n', content)

# Compress content variable
bz_compressed = BZ2Compressor().compress(content)

# Get the length of the compressed variable
print("Content:", len(bz_compressed))

# Decompress variable
bz_decompressed = BZ2Decompressor().decompress(bz_compressed)

# Print the content and length of the decompressed variable
print("Decompressed content:", len(bz_decompressed))
