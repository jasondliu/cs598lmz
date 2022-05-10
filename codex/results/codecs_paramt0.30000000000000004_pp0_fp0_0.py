import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_file(filename):
    return codecs.open(filename, encoding='utf-8', errors='strict')

def get_file_lines(filename):
    return get_file(filename).readlines()

def get_file_contents(filename):
    return get_file(filename).read()

def get_file_json(filename):
    return json.loads(get_file_contents(filename))

def get_file_yaml(filename):
    return yaml.load(get_file_contents(filename))

def get_file_csv(filename):
    return list(csv.reader(get_file_lines(filename)))

def get_file_tsv(filename):
    return list(csv.reader(get_file_lines(filename), delimiter='\t'))

def get_file_ssv(filename):
    return list(csv.reader(get_file_lines(filename), delimiter=';'))

def get_file_psv(filename):
   
