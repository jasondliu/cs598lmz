import bz2
# Test BZ2Decompressor class
with bz2.open('/media/storage/Webscope/ydata-fp-td-clicks-v1_0/ydata-fp-td-clicks-v1_0.txt.bz2', 'rb') as infile:
    with open('dummy.txt', 'wb') as oufile:
        decompressor = bz2.BZ2Decompressor()
        while True:
            data = infile.read(1024)
            if not data:
                break
            oufile.write(decompressor.decompress(data))


#file_in = bz2.BZ2File('/media/storage/Webscope/ydata-fp-td-clicks-v1_0/ydata-fp-td-clicks-v1_0.txt.bz2') # open for reading
#file_out = open('dummy.txt', 'wb') # open for writing

#decompressor = bz2.BZ2Decompressor()

#for data in iter(lambda : file_in.read(100
