from bz2 import BZ2Decompressor
BZ2Decompressor.__module__ = 'bz2'

# Tell the user what's going on.
write("Extracting %s...\n" % (filename))

# Set up the extraction.
file = BZ2File(filename)
makedirs(extract_dir)

# Extract to stdout.
while 1:
    data = file.read(100000)
    if len(data) == 0:
        break
    write(data)
    
write("Done.\n")
