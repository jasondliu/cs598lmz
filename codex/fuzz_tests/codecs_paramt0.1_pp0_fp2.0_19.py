import codecs
codecs.register_error('strict', codecs.ignore_errors)

def read_file(filename):
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        return f.read()

def write_file(filename, data):
    with codecs.open(filename, 'w', 'utf-8', 'strict') as f:
        f.write(data)

def read_json(filename):
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        return json.load(f)

def write_json(filename, data):
    with codecs.open(filename, 'w', 'utf-8', 'strict') as f:
        json.dump(data, f, indent=4, sort_keys=True)

def read_yaml(filename):
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        return yaml.load(f)

def write_yaml(filename, data):
    with codec
