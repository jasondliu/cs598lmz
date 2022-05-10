import bz2
# Test BZ2Decompressor
bz2_decompressor = bz2.BZ2Decompressor()

# Decompress the compressed file
decompressed_data = bz2_decompressor.decompress(compressed_data)

# Decode the decompressed data and print the result.
decoded_data = decompressed_data.decode("utf-8")
print(decoded_data)

# Write the decompressed data to a file.
with open("decompressed_wiki.xml", "wb") as file:
    file.write(decompressed_data)

print("Done.")

#With the bz2.BZ2Compressor and bz2.BZ2Decompressor

# Create a BZ2Compressor object.
bz2_compressor = bz2.BZ2Compressor()

# Compress the input data.
bz_compressed_data = bz2_compressor.compress(input_data)

# Finish the compression process.
bz_compressed_data += bz2_compressor.flush()


