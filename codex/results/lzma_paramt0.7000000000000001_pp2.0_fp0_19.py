from lzma import LZMADecompressor
LZMADecompressor.BEST_COMPRESSION

def extract_data(filename):
    with open(filename, "rb") as f:
        data = f.read()
        decompressor = LZMADecompressor()
        result = decompressor.decompress(data)
        return result


def extract_and_load_data(filename):
    result = extract_data(filename)
    return np.load(io.BytesIO(result))

# load the data
x_train = extract_and_load_data("../data/x_train.pkl")
y_train = extract_and_load_data("../data/y_train.pkl")
x_test = extract_and_load_data("../data/x_test.pkl")
y_test = extract_and_load_data("../data/y_test.pkl")

x_train = x_train[:,:,:,1].reshape(-1,28,28,1)
x_test = x_test[:,:,:,1].reshape(-1,28,28,1)
x_
