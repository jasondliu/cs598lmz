from bz2 import BZ2Decompressor
BZ2Decompressor

from itertools import islice
import sys

window = 200
step = 50
process_size = 500000
infilename = sys.argv[1]

with open(infilename, "rb") as input_data:
    while True:
        process_data = input_data.read(process_size)
        if not process_data:
            break

        #pickle_file = open("sensor_pickle_size_500000.pickle", "wb")
        #pickle.dump(process_data, pickle_file)
        #pickle_file.close()
        #pickle_stream = open("sensor_pickle_size_500000.pickle", "rb")
        bz2_data_out = bz2.decompress(process_data)
        #bz2_data_out = bz2.decompress(pickle_stream.read())
        #pickle_stream.close()
        bz2_data_out_UTF8 = str(bz2_data_out, 'utf-8')

