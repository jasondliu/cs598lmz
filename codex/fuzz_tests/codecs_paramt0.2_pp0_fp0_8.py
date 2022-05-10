import codecs
codecs.register_error('strict', codecs.ignore_errors)

def read_file(filename):
    with codecs.open(filename, encoding='utf-8', errors='strict') as f:
        return f.read()

def write_file(filename, data):
    with codecs.open(filename, 'w', encoding='utf-8', errors='strict') as f:
        f.write(data)

def read_json(filename):
    with open(filename) as f:
        return json.load(f)

def write_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, sort_keys=True)

def read_yaml(filename):
    with open(filename) as f:
        return yaml.load(f)

def write_yaml(filename, data):
    with open(filename, 'w') as f:
        yaml.dump(data, f, default_flow_style=False)

def read_csv(filename):
    with open
