from bz2 import BZ2Decompressor
BZ2Decompressor.max_size = int(7e9)

def read_fastq(data_files, data_type=float32, min_num_read = 0):
    '''Read data file and return a dictionary of data_file, number of read and size'''
    dic = {}
    try:
        new_size = 0
        with BZ2File(data_files[0], 'r') as f:
            n = 0
            for l in f:
                n  += 1
                l = l.rstrip("\r\n")
                parts = l.split("\t")
                if n == 1:
                    try:
                        new_size += int(parts[0]) + int(parts[2])
                    except Exception:
                        new_size += int(parts[3])
        f.close()
    except Exception:
        new_size = 0
        
    for data_file in data_files:
        new_size += os.stat(data_file).st_size
        data_dic = {}
        try:
            # compression gzip
           
