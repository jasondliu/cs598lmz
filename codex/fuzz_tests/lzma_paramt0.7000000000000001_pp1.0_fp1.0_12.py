from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed)

# for more information about the LZMA problem see https://stackoverflow.com/questions/31631038/lzma-error-bad-input-length-when-trying-to-decompress
# and https://stackoverflow.com/questions/20682142/how-to-compress-a-string-in-python-3-using-lzma

# if this does not work, you can try the following
# decompressed = bz2.decompress(compressed)
# decompressed = gzip.decompress(compressed)

# the result is a binary string
# you can convert it into a string
# decoded = decompressed.decode("utf-8")
# and print it
# print(decoded)

# or you can write it to a file
# with open("decompressed.txt", "wb") as f:
#    f.write(decompressed)
