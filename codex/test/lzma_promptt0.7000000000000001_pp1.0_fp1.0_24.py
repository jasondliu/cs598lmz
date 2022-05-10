import lzma
# Test LZMADecompressor for subprocess.Popen
# https://docs.python.org/3/library/lzma.html

# Get a file from the Internet
url = 'https://www.python.org/static/img/python-logo.png'

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Open the url with urllib.request, and read all its data
