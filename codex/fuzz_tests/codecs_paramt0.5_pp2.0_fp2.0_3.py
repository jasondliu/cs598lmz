import codecs
codecs.register_error('strict', codecs.lookup_error('replace'))

class File:
    def __init__(self, file_name, file_path):
        self.file_name = file_name
        self.file_path = file_path
        self.file_contents = []

    def open_file(self):
        with codecs.open(self.file_path, 'r', encoding='utf8', errors='strict') as f:
            self.file_contents = f.readlines()

    def get_file_contents(self):
        return self.file_contents

    def get_file_name(self):
        return self.file_name

    def get_file_path(self):
        return self.file_path
