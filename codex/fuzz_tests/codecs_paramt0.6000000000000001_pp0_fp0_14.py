import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

class ReadCSV():

    def __init__(self, file, delimiter):
        self.file = file
        self.delimiter = delimiter

    def read(self):
        with open(self.file) as csvfile:
            reader = csv.reader(csvfile, delimiter=self.delimiter)
            next(reader, None)  # skip the headers
            for row in reader:
                # print row
                yield row


class ReadXLSX():

    def __init__(self, file):
        self.file = file

    def read(self):
        wb = load_workbook(filename=self.file, read_only=True)
        ws = wb.active
        for row in ws.rows:
            yield [cell.value for cell in row]


class ReadJSON():
    def __init__(self, file):
        self.file = file

    def read(self):
        with open(self.file) as json_data:
