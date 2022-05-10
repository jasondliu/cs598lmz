import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)


class Txt:
    def __init__(self, path):
        self.path = path
        self.lst = []
        self.load()

    def load(self):
        with open(self.path, 'r') as f:
            for line in f.readlines():
                self.lst.append(line.split())

    def get_list(self):
        return self.lst

    def print_list(self):
        for i in self.lst:
            print(i)

    def get_column(self, col):
        return [item[col] for item in self.lst]

    def get_column_with_index(self, col):
        return [(idx, item[col]) for idx, item in enumerate(self.lst)]

    def get_row(self, row):
        return self.lst[row]

    def update_cell(self, row, col, value):

