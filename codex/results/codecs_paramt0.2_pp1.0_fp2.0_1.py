import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_data(filename):
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        return f.read()

def get_data_lines(filename):
    return get_data(filename).split('\n')

def get_data_json(filename):
    return json.loads(get_data(filename))

def get_data_csv(filename):
    return list(csv.reader(get_data_lines(filename)))

def get_data_tsv(filename):
    return list(csv.reader(get_data_lines(filename), delimiter='\t'))

def get_data_pickle(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

def get_data_yaml(filename):
    return yaml.load(get_data(filename))

def get_data_xml(filename):
    return ET.parse(filename)

def get_data_html(filename
