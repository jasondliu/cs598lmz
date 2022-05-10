from lzma import LZMADecompressor
LZMADecompressor().decompress(resp.content)

# to get the first 10,000 bytes
resp.raw.read(10000)

# to get the whole thing
resp.raw.read()

# to get the whole thing in memory
resp.content

# to get the whole thing in memory
resp.text

# to get the whole thing in memory
resp.json()

# to get the whole thing in memory
resp.headers

# to get the whole thing in memory
resp.status_code

# to get the whole thing in memory
resp.url

# to get the whole thing in memory
resp.headers['Content-Type']

# to get the whole thing in memory
resp.headers.get('Content-Type')

# to get the whole thing in memory
resp.headers.get('content-type')

# to get the whole thing in memory
resp.headers.get('Content-type')

# to get the whole thing in memory
resp.headers['content-type']


# to get the whole thing in memory
resp.headers.get('content-type', 'application/
