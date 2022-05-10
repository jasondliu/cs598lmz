from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# write to file
with open("/tmp/output.bz2", "wb") as f:
    f.write(data)
</code>
This code works fine, but it is not the most efficient way to do it.
The following code is much faster:
<code>import requests
import bz2

# download the file
url = "https://www.dropbox.com/s/6m7v6p8w6o4f7pz/test.bz2?dl=1"
r = requests.get(url, stream=True)

# write to file
with open("/tmp/output.bz2", "wb") as f:
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            f.write(chunk)

# decompress
with open("/tmp/output.bz2", "rb") as f:
    decompressor = bz2.BZ2Decompressor()
    for data in iter(lambda : f.read(100 * 1024), b
