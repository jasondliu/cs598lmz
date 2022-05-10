import bz2
# Test BZ2Decompressor
d = bz2.BZ2Decompressor()
data = d.decompress(data)

print(data)
</code>
The last line gives the response <code>b'{"the field you want":"the data you want"}'</code>
and then you can use the json.loads() method of the json library to parse it into a dict that you can later use.

