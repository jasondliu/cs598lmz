import mmap

# This should be the name of the file with the XML metadata
metadata_filename="metadata.xml"

# This one is the ID of the first WAD chunk
chunk_id = 0

# This one is the number of the last chunk to include
chunk_count = 0

# This should be the name of the output file
wad_filename="output.wad"


# XXX No error checking. Use at your own risk!

n = 0

wad_file = open(wad_filename, "wb")

for i in range(chunk_count):
    f = open(wad_filename.replace(".wad", ".%d.wad") % i, "rb")
    mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    wad_file.write(mm.read())
    f.close()
    mm.close()

wad_file.close()
