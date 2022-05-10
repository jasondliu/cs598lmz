import codecs
codecs.register_error('strict', codecs.ignore_errors)

def _read_file(filename):
    try:
        with codecs.open(filename, 'r', 'utf-8') as f:
            return f.read()
    except UnicodeDecodeError as e:
        with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
            return f.read()

def _write_file(filename, data):
    with codecs.open(filename, 'w', 'utf-8') as f:
        f.write(data)

class File(object):
    def __init__(self, filename):
        self.filename = filename
        self.data = _read_file(filename)

    def save(self):
        _write_file(self.filename, self.data)

if __name__ == '__main__':
    f = File('/tmp/test.txt')
    print f.data
    f.data = f.data + '\nhello world'
    f.save()
