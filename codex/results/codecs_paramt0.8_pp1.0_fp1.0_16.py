import codecs
codecs.register_error('strict', codecs.lookup_error('ignore'))

"""
This file implements the csv_class
which takes an csv file and standardize it into a table form
with the column names at the top row of the table
"""
class csv_class(object):
    def __init__(self, file_location):
        self.file_location = file_location
        self.column_names = []
        self.table = []
        self.raw_table = []

    def open_csv(self):
        with open(self.file_location, 'rb') as f:
            temp = csv.reader(f)
            for row in temp:
                self.table.append(row)
            f.close()

    def standardize_columns(self):
        self.column_names = self.table[0]
        self.table = self.table[1:]

    def write_to_csv(self):
        table_writer = csv.writer(open('temp.csv', 'w+'))
        for row in self.table:
            table
