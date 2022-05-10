import bz2
bz2_compress_obj = bz2.BZ2Compressor()

def bz2_compress(string):
    return bz2_compress_obj.compress(string) + bz2_compress_obj.flush()

if __name__ == '__main__':
    fh = open("compress_test_file", "r")
    test_string = fh.read()
    compressed_string = bz2_compress(test_string)
    print "Uncompressed (length):\t{0}".format(len(test_string))
    print "Compressed (length):\t{0}".format(len(compressed_string))
    print "Saved:\t\t\t{0}".format((1.0 - float(len(compressed_string))/len(test_string)))
