from lzma import LZMADecompressor
LZMADecompressor(format=FORMAT_ALONE)

print("\nDecompressing data...\nPlease wait a while")
data = decompressor.decompress(data)

print("Done.\n")

print("Writing the data...")
with open(target, "wb") as f:
    f.write(data)

print('All Done, enjoy it!')
