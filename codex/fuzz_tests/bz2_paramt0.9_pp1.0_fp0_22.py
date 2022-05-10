from bz2 import BZ2Decompressor
BZ2Decompressor

###############################################################################

with open('output/vectors.txt', 'r') as file:

    # read lines one by one
    for line in file:
        # print(line)
        vector = line.split('\t')
        print(len(vector))
        print(len(vector[1]))
        # read vector

        exit()

###############################################################################

with open('output/vectors.txt', 'rb') as file:

    # read lines one by one
    for line in file:
        # print(line)
        vector = line.split('\t')
        print(len(vector))
        print(len(vector[1]))
        # read vector

        exit()

###############################################################################

with bz2.BZ2File('output/training-v1/offenseval-training-v1.tsv.zip') as file:
    uncompressed_data = file.read()
    # print(uncompressed_data)
    # print(uncompressed_data.decode('utf-8').split
