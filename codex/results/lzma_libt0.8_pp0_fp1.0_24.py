import lzma
lzma = LZMADecompressor()

def load_train_data(file, size_limit=999999999):
    with lzma.open(file) as fopen:
        train = fopen.read(size_limit)
        return re.split(b'\n', train)

def load_test_data(file, size_limit=999999999):
    with lzma.open(file) as fopen:
        test = fopen.read(size_limit)
        return re.split(b'\n', test)

def get_watch(seconds, title=None):
    start = time.time()
    h, m, s = 0, 0, 0
    while True:
        counts = int(time.time() - start)
        m, s = divmod(counts, 60)
        h, m = divmod(m, 60)
        watched = '%02d:%02d:%02d' % (h, m, s)
        os.system('clear')
        if title is not None: print(title
