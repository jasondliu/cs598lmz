import codecs
codecs.register_error('strict', codecs.ignore_errors)

class CsvReader(object):
    def __init__(self, file_name, delimiter=',', quotechar='"'):
        self.file_name = file_name
        self.delimiter = delimiter
        self.quotechar = quotechar

    def __enter__(self):
        self.csv_file = open(self.file_name, 'rb')
        self.csv_reader = csv.reader(self.csv_file, delimiter=self.delimiter, quotechar=self.quotechar)
        return self

    def __exit__(self, type, value, traceback):
        self.csv_file.close()

    def next(self):
        return self.csv_reader.next()

    def __iter__(self):
        return self

class CsvWriter(object):
    def __init__(self, file_name, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL):
        self.file_name = file_name
        self.delim
