import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def unicode_csv_reader(unicode_csv_data, dialect=csv.excel, **kwargs):
    # csv.py doesn't do Unicode; encode temporarily as UTF-8:
    csv_reader = csv.reader(utf_8_encoder(unicode_csv_data),
                            dialect=dialect, **kwargs)
    for row in csv_reader:
        # decode UTF-8 back to Unicode, cell by cell:
        yield [unicode(cell, 'utf-8') for cell in row]

def utf_8_encoder(unicode_csv_data):
    for line in unicode_csv_data:
        yield line.encode('utf-8')

def read_csv_file(file_name):
    with open(file_name, 'rb') as f:
        reader = unicode_csv_reader(f)
        for row in reader:
            print row

def get_csv_data(file_name):
    data =
