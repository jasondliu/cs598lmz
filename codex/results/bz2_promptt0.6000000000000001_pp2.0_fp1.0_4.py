import bz2
# Test BZ2Decompressor to read in compressed files

# Decompress the file
with bz2.BZ2Decompressor() as decompressor:
    with open("enwiki-latest-pages-articles1.xml-p10p30302.bz2", 'rb') as input, open("enwiki-latest-pages-articles1.xml-p10p30302.xml", 'wb') as output:
        for data in iter(lambda : input.read(100 * 1024), b''):
            output.write(decompressor.decompress(data))

# Open the file
with open("enwiki-latest-pages-articles1.xml-p10p30302.xml", 'rb') as i:
    xml = i.read()
# Sample the first 100 bytes of the XML file
xml[:100]

# Check the first article
xml.find(b"<page>")

# Check the last article
xml.rfind(b"</page>")

# Write the contents to disk
with open("enwiki-latest-pages-articles1.xml-p10p30302.xml
