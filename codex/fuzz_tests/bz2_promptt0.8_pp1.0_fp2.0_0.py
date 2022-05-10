import bz2
# Test BZ2Decompressor
import io
decomp = bz2.BZ2Decompressor()
infile = io.BufferedReader(bz2.open("lorem_ipsum.bz2", "rb"))
outfile = io.BytesIO()

# Read small chunks
while True:
    data = infile.read(1024)
    if not data:
        break
    outfile.write(decomp.decompress(data))

    # Flush data to output file
    if outfile.tell() > 10240:
        break

with open("lorem_ipsum.txt", "wb") as f:
    f.write(outfile.getvalue())
outfile.close()
with open("lorem_ipsum.txt", "r") as f:
    print(f.read())

# Test BZ2Compressor
comp = bz2.BZ2Compressor(9)
infile = io.BufferedReader(open("lorem_ipsum.txt", "rb"))
outfile = io.BytesIO()

while True:
    data = infile
