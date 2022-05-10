import bz2
# Test BZ2Decompressor
# http://stackoverflow.com/questions/27981545/suppress-warning-unclosed-file-<_io-bufferedreader-name-rb-at-0x7f25d0c5b438
import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    decompressor = bz2.BZ2Decompressor()
    with open('train.ft.txt.bz2', 'rb') as f_in, open('train.ft.txt', 'wb') as f_out:
        for data in iter(lambda: f_in.read(100 * 1024), b''):
            f_out.write(decompressor.decompress(data))
# Read train data
with open('train.ft.txt', 'r') as f:
    train_data = f.read().splitlines()
# Read test data
with open('test.ft.txt', 'r') as f:
    test_data = f.read().splitlines()
# Read unlabeled data
with open('unlabeledTrain.ft.txt
