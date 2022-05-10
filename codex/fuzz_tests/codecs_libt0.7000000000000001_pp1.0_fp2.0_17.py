import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

def read_data(filename, delimiter=','):
    with open(filename) as data:
        lines = data.readlines()
        return [line.strip().split(delimiter) for line in lines]

def get_key(file):
    return os.path.splitext(file)[0]

def get_files(path, extension='.csv'):
    files = glob.glob(path + '\\*' + extension)
    return dict(zip(map(get_key, files), files))

def get_all_files(path, extension):
    return {key: get_files(path + '\\' + key, extension) for key in os.listdir(path)}


def load_data(path, extension='.csv'):
    return {key: read_data(file) for key, file in get_files(path, extension).items()}

def load_all_data(path, extension='.csv'
