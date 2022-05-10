import codecs
codecs.register_error('surrogate_escape', codecs.surrogateescape_error)

def read_file(filename):
    with codecs.open(filename, 'r', 'utf-8', 'surrogate_escape') as f:
        return f.read()

def write_file(filename, data):
    with codecs.open(filename, 'w', 'utf-8', 'surrogate_escape') as f:
        f.write(data)

def read_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def write_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def read_yaml(filename):
    with open(filename, 'r') as f:
        return yaml.load(f)

def write_yaml(filename, data):
    with open(filename, 'w') as f:
        yaml.dump(data, f, default_flow_style=False)


