from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open('./tmp/train.bz2').read())

# decompress train data
def read_compressed_data(filename, decompress=True):
    """
    Read a compressed file, decompressing on the fly (bz2)
    """
    if decompress:
        file = BZ2File(filename)
    else:
        file = open(filename, 'rb')

    data = b''
    try:
        for line in file:
            data += line
        file.close()
    except EOFError:
        file.close()
    return data

# decompress train data
train_decompressed = read_compressed_data('./tmp/train.bz2')

# write train data
open('./tmp/train.json','wb').write(train_decompressed)

# read train data
train = pd.read_json('tmp/train.json')

# delete the original train data
import os
os.remove('tmp/train.json')
X_train = train.desc.values
y
