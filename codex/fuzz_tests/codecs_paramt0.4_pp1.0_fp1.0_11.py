import codecs
codecs.register_error('strict', codecs.ignore_errors)

def read_file(filename):
    with codecs.open(filename, encoding='utf-8', errors='strict') as f:
        return f.read()

def write_file(filename, contents):
    with codecs.open(filename, 'w', encoding='utf-8', errors='strict') as f:
        f.write(contents)

def read_json(filename):
    return json.loads(read_file(filename))

def write_json(filename, data):
    write_file(filename, json.dumps(data, indent=4, sort_keys=True))

def read_yaml(filename):
    return yaml.load(read_file(filename))

def write_yaml(filename, data):
    write_file(filename, yaml.dump(data, default_flow_style=False))

def read_csv(filename, delimiter=','):
    with open(filename) as f:
        return [l.strip().split(delimiter) for l in
