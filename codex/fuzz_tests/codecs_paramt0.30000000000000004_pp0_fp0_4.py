import codecs
codecs.register_error('strict', codecs.ignore_errors)

def read_file(filename):
    with codecs.open(filename, encoding='utf-8', errors='strict') as f:
        return f.read()

def write_file(filename, data):
    with codecs.open(filename, 'w', encoding='utf-8', errors='strict') as f:
        f.write(data)

def read_json(filename):
    return json.loads(read_file(filename))

def write_json(filename, data):
    write_file(filename, json.dumps(data, indent=2, sort_keys=True))

def read_yaml(filename):
    return yaml.load(read_file(filename))

def write_yaml(filename, data):
    write_file(filename, yaml.dump(data, default_flow_style=False))

def read_toml(filename):
    return toml.loads(read_file(filename))

def write_toml(filename, data):
    write_file(
