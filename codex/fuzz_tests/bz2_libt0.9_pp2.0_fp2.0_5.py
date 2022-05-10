import bz2
bz2_xml = b""
with open("example.xml.bz2", "rb") as f:
    bz2_xml = f.read()

 
print("The length of the compressed data is", len(bz2_xml))
print("The first 300 characters are", bz2_xml[:300])
print("The last 300 characters are", bz2_xml[-300:])

# convert to text format
xml = bz2.decompress(bz2_xml)
print("The uncompressed data is", len(xml), "characters long.")
