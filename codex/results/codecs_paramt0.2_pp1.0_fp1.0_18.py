import codecs
codecs.register_error('strict', codecs.ignore_errors)

class File(object):
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.open_file = codecs.open(self.filename, self.mode, encoding='utf-8', errors='strict')
        return self.open_file

    def __exit__(self, *args):
        self.open_file.close()

files = ['cats.txt', 'dogs.txt']

for file in files:
    try:
        with File(file) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        pass
