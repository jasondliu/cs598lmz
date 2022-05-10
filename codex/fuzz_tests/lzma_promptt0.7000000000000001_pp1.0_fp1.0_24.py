import lzma
# Test LZMADecompressor for subprocess.Popen
# https://docs.python.org/3/library/lzma.html

# Get a file from the Internet
url = 'https://www.python.org/static/img/python-logo.png'

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Open the url with urllib.request, and read all its data
with urllib.request.urlopen(url) as src, \
        open('python-logo.xz', 'wb') as dst_xz, \
        open('python-logo.png', 'wb') as dst_orig:
    while True:
        block = src.read(1024)
        if not block:
            break
        dst_xz.write(block)
        dst_orig.write(decompressor.decompress(block))
    dst_orig.write(decompressor.flush())


"""
# Same thing as above, but using a context manager
with urllib.request.urlopen(url) as src,
