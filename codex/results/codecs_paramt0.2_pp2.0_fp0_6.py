import codecs
codecs.register_error('strict', codecs.ignore_errors)

def read_file(filename):
    with codecs.open(filename, encoding='utf-8', errors='strict') as f:
        return f.read()

def write_file(filename, contents):
    with codecs.open(filename, 'w', encoding='utf-8', errors='strict') as f:
        f.write(contents)

def read_json(filename):
    with open(filename) as f:
        return json.load(f)

def write_json(filename, contents):
    with open(filename, 'w') as f:
        json.dump(contents, f, indent=4, sort_keys=True)

def read_yaml(filename):
    with open(filename) as f:
        return yaml.load(f)

def write_yaml(filename, contents):
    with open(filename, 'w') as f:
        yaml.dump(contents, f, default_flow_style=False)

def read_csv(filename, delim
