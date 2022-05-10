import mmap
# Test mmap.mmap(fileno, length,
#                flags=MAP_SHARED,
#                prot=PROT_WRITE | PROT_READ,
#                access=ACCESS_DEFAULT [, offset])
access_mode = mmap.ACCESS_READ # ACCESS_COPY
offset = 0xdeadbeef
length = 0x1000
prot = mmap.PROT_WRITE
flags = mmap.MAP_SHARED
write_buf = b"This is some data to write"
read_buf = b"This is a place to read into"

# The file must exist.
filename = "./test.mm.file"
if os.path.isfile(filename):
    print("Removing existing file")
    os.remove(filename)

print("Creating new file")
fid = open(filename, 'w')

print("Writing initial buffer")
fid.write(write_buf)

print("Closing file")
fid.close()

print("Using mmap to map file")
nfid = mmap.mmap(fid.fileno
