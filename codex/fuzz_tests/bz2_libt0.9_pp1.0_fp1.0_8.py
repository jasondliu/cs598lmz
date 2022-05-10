import bz2
bz2_comp = bz2.BZ2Compressor() # creates a compresser object which will be used below
with open('espanol/news.train.es-en.es', "r") as file_handle:    
    with open('news.train.es-en.es.bz2',"wb") as output_handle: # create an output file handle and specify the format as binary
        inside_doc=False
        # loop over each line in the input file
        while True:
            line = file_handle.readline() # get one line at a time from the file
            # break if eof
            if line == '':
                break 

            # compress each line seperately and then write the compressed output to file
            line_bz2 = bz2_comp.compress(line.encode())
            output_handle.write(line_bz2)

#print 'size before bz2 compression:', os.path.getsize('espanol/news.train.es-en.en')
#print 'size after bz2 compression:', os.path.gets
