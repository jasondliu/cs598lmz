import lzma
# Test LZMADecompressor:
#dcomp = lzma.decompressobj()
#infile = open('c:\\teste.rmvb', 'rb')
#while True:
#    block = infile.read(10240)
#    if not block:
#        break
#    uncomp = dcomp.decompress(block)
#    sys.stdout.write(uncomp)
#infile.close()


# ftree[0] = 'c:\\teste2.rmvb'
# ftree[1] = 'c:\\teste4.rmvb'
# ftree[2] = 'c:\\teste2.txt'
# ftree[193] = 'c:\\teste3.rmvb'

def doTest ():
    cmp = lzma.compressobj()
    for each in ftree.iterkeys():
        try:
            infile = open (ftree[each], 'rb')
        except IOError:
            continue
        while True:
            block = infile.read(10240)
