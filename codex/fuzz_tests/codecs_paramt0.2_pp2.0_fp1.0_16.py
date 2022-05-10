import codecs
codecs.register_error('strict', codecs.ignore_errors)

def read_file(filename):
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        return f.read()

def write_file(filename, content):
    with codecs.open(filename, 'w', 'utf-8', 'strict') as f:
        f.write(content)

def read_json(filename):
    return json.loads(read_file(filename))

def write_json(filename, content):
    write_file(filename, json.dumps(content, indent=2, sort_keys=True))

def read_yaml(filename):
    return yaml.load(read_file(filename))

def write_yaml(filename, content):
    write_file(filename, yaml.dump(content, default_flow_style=False))

def read_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        return list(reader)

def
