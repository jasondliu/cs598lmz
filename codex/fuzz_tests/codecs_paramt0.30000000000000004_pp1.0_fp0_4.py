import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_data(infile):
    with codecs.open(infile, 'r', 'utf-8', 'strict') as f:
        data = f.read()
    return data

def get_data_lines(infile):
    with codecs.open(infile, 'r', 'utf-8', 'strict') as f:
        data = f.readlines()
    return data

def write_data(outfile, data):
    with codecs.open(outfile, 'w', 'utf-8', 'strict') as f:
        f.write(data)

def write_data_lines(outfile, data):
    with codecs.open(outfile, 'w', 'utf-8', 'strict') as f:
        f.writelines(data)

def get_file_list(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for f in files:
            if f.endswith('.
