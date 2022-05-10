import bz2
bz2.decompress(bz2_compressed_data)

def decompress_bz2_file(input_filepath, output_filepath):
    bz2_compressed_data = open(input_filepath, 'rb').read()
    data = bz2.decompress(bz2_compressed_data)
    open(output_filepath, 'wb').write(data)

decompress_bz2_file('input.txt.bz2', 'output.txt')

import bz2
def compress_bzip2(data):
    #compressor = bz2.BZ2Compressor()
    #compressed_data = compressor.compress(data)
    #compressed_data += compressor.flush()    
    #return compressed_data
    return bz2.compress(data)
 
def decompress_bzip2(compressed_data):
    #decompressor = bz2.BZ2Decompressor()
    #decompressed_data = decompressor.decompress(compressed_data)
