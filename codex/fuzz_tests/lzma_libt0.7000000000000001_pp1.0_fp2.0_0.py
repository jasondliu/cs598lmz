import lzma
lzma.open()
os.path
def load_lzma_dataset(dataset_path):
    print('uncompressing dataset...')
    with lzma.open(dataset_path, 'rb') as f:
        data = pickle.load(f)
    print('uncompressing done.')
    return data

dataset_path = 'dataset/pickle_data_train.lzma'

data_train = load_lzma_dataset(dataset_path)

data_train[0]

data_train[0][0].shape
data_train[0][1].shape

data_train[0][0]
data_train[0][1]

data_train[1][0].shape
data_train[1][1].shape

data_train[1][0]
data_train[1][1]

data_train[2][0].shape
data_train[2][1].shape

data_train[2][0]
data_train[2][1
