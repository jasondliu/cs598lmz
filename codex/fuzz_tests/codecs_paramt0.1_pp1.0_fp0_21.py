import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_file_path(filename):
    return os.path.join(os.path.dirname(__file__), filename)

def get_file_contents(filename):
    with codecs.open(get_file_path(filename), 'r', 'utf-8', 'strict') as f:
        return f.read()

def get_file_contents_as_lines(filename):
    return get_file_contents(filename).splitlines()

def get_file_contents_as_json(filename):
    return json.loads(get_file_contents(filename))

def get_file_contents_as_yaml(filename):
    return yaml.load(get_file_contents(filename))

def get_file_contents_as_csv(filename):
    return csv.reader(get_file_contents(filename).splitlines())

def get_file_contents_as_csv_dict(filename):
    return csv.DictReader(get
