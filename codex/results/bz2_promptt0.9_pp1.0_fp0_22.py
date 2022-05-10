import bz2
# Test BZ2Decompressor and BZ2Compressor

# compress a file and decompress it
outfilename = 'test.txt.bz2'
with open('file_6MB.log', 'r') as infile, \
     bz2.open(outfilename, 'w') as outfile:
    outfile.writelines(infile)

with bz2.open(outfilename, 'r') as infile, \
     open('file_6MB.log.decompressed', 'w') as outfile:
    outfile.writelines(infile)

# compress a file with a compressor object
outfilename = 'test.txt.bz2'
with open('file_6MB.log', 'r') as infile, \
     bz2.BZ2Compressor().open(outfilename, 'w') as comp, \
     bz2.open(outfilename, 'r') as decomp:
    for line in infile:
        comp.write(line)
    # have to close the compressor since it adds some stuff
    comp.close()
    decomp.seek(0)
