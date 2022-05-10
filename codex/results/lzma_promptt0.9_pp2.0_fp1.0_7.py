import lzma
# Test LZMADecompressor
# eg. bz2.decompress(data)
# where data must be the object consisting entirely of compressed data.

def read_lzma(filename, fn_size, num_files, f, buff_size=1024):
    print "Reading in LZMA file..."
    with open(filename, 'rb') as f:
        dcom = lzma.LZMADecompressor()
        LzmaReader(dcom)
        for i in range(num_files):
            print "Extracting file {} out of {} files...".format(i+1, num_files)
            with open('TEST' + str(i) + '.txt.gz', 'wb') as out_file:
                while 1:
                    data = f.read(buff_size)
                    if not data:
                        break
                    out_file.write(dcom.decompress(data))
        out_file.close()
    f.close()
    print "Done."    
    
#read_lzma('pages.txt.sig', 8222852, 10000
