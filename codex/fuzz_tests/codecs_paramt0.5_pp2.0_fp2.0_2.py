import codecs
codecs.register_error('strict', codecs.ignore_errors)

class FileIO:
    def __init__(self, file_name):
        self.file_name = file_name

    def write_to_file(self, data):
        with open(self.file_name, 'w', encoding='utf-8') as f:
            f.write(data)

    def read_from_file(self):
        with open(self.file_name, 'r', encoding='utf-8') as f:
            return f.read()


class FileIO_json(FileIO):
    def write_to_file(self, data):
        with open(self.file_name, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)

    def read_from_file(self):
        with open(self.file_name, 'r', encoding='utf-8') as f:
            return json.load(f)


class FileIO_csv(FileIO):
    def write_to_file(self,
