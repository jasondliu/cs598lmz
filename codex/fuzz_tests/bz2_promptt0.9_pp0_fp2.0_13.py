import bz2
# Test BZ2Decompressor
print("Creating decompressor object...", end="")
decompressor = bz2.BZ2Decompressor()
print("done.")
print("Uncompressing...", end="")
text = decompressor.decompress(compressedData)
print("done.")
print("Decompressed size:", len(text))
print("Original size:", originalSize)
print("Verifying...", end="")
if text == originalText:
    print("done.")
else:
    print(end=" Failed!\n")

print()
if len(text) != originalSize:
    raise RuntimeError("Decompressed data does not match the original")
 
# Test BZ2File
print("Creating compressed file...", end="")
compressedFilePath = "bz2file.bz2"
compressedFile = bz2.BZ2File(compressedFilePath, "wb")
print("done.")

print("Writing to compressed file...", end="")
compressedFile.write(originalText)
print("done.")
print("Flushing and closing file...", end="
