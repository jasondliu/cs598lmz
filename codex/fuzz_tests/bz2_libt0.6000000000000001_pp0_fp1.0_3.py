import bz2
bz2_file = bz2.BZ2File('wiki.xml.bz2')

# or, if you prefer
import bz2
bz2_file = bz2.BZ2File('wiki.xml.bz2','rb')

# Decompress the file into a new file named "wiki.xml"

#bz2_file = bz2.open('wiki.xml.bz2', 'rb')
bz2_file = bz2.BZ2File('wiki.xml.bz2')
output = open('wiki.xml', 'wb')
for data in iter(lambda : bz2_file.read(100 * 1024), b''):
    output.write(data)
output.close()
bz2_file.close()


# After decompressing the file, the file size is 25.8G, which is larger than the size of my memory, so I can't load the xml file into the memory.
# But I can still use the xml.etree.ElementTree to parse the xml file, it doesn't need to load the whole xml file
