import codecs
codecs.register_error('strict', codecs.ignore_errors)


class FileManager:
    def __init__(self, locations):
        self.locations = locations
        self.files = {}
        for loc in self.locations:
            self.files[loc] = {}

    def open(self, location, filename, mode='r', encoding='utf8'):
        if location in self.files and filename in self.files[location]:
            return self.files[location][filename]
        if location in self.locations:
            filepath = os.path.join(self.locations[location], filename)
            f = filedb.open(filepath, mode, encoding)
            self.files[location][filename] = f
            return f
        return None

    def get_path(self, location, filename):
        filepath = os.path.join(self.locations[location], filename)
        return filepath

    def close(self, location, filename):
        if location in self.files and filename in self.files[location]:
            self.files[location][filename].close()
