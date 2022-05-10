import codecs
codecs.register_error('strict', codecs.ignore_errors)

class File(object):
    def __init__(self, path, mode='r', encoding='utf-8', errors='strict'):
        self.path = path
        self.mode = mode
        self.encoding = encoding
        self.errors = errors
        self.file = codecs.open(path, mode, encoding, errors)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

with File('test.txt', 'w', 'utf-8', 'ignore') as f:
    f.write('test')

with File('test.txt', 'r', 'utf-8', 'ignore') as f:
    print(f.read())

# 上下文管理器的一个重要特性是它们可以使用 with 语句。
# 上下文
