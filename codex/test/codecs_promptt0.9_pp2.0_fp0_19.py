import codecs
# Test codecs.register_error('test', lambda *args: ' ') to replace utf8 error with a space
# codecs.register_error('test', lambda *args: unicodedata.normalize('NFKD', u'\ufffd'))

def load_csvjson(file_name, encoding='utf-8', verbose=False):
    # This try/except only works with .csv and .json
    try:
        if not file_name.endswith('.csv') and not file_name.endswith('.json'):
            raise Exception('Invalid input file: %s' % file_name)
    except:
        print ('Invalid input file: %s' % file_name)
        return

    file_extension = os.path.splitext(file_name)[1]
    print (file_extension)
    data=[]
    if 'csv' == file_extension:
        with open(file_name, encoding=encoding) as f:
            reader = csv.reader(f)
