import bz2
# Test BZ2Decompressor by decompressing all blocks in a file, checking for errors.

for test_file in sys.argv[1:]:
    print "Testing file", test_file, "...",

    f = bz2.BZ2File(test_file)
    try:
        decomp = bz2.BZ2Decompressor()
        while 1:
            input = f.read(1024)
            if not input:
                break
            output = decomp.decompress(input)
    except IOError:
        print "failed"
    else:
        
