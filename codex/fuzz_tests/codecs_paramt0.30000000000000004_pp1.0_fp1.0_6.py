import codecs
codecs.register_error('strict', codecs.ignore_errors)

class JsonFile(object):
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except IOError:
            print 'IOError: %s' % self.file_path
        except ValueError:
            print 'ValueError: %s' % self.file_path

    def write(self, data):
        with open(self.file_path, 'w') as f:
            json.dump(data, f)

class CsvFile(object):
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        try:
            with open(self.file_path, 'r') as f:
                reader = csv.reader(f)
                return [row for row in reader]
        except IOError:
            print 'IOError:
