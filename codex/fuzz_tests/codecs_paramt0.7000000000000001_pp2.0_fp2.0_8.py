import codecs
codecs.register_error('strict', codecs.ignore_errors)

def handle_error(msg):
    """ Handle encoding errors and return a string
    """
    return 'error: %s' % msg

codecs.register_error('strict', handle_error)

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

#def create_user(username, password, email):
#    user = User.objects.create
