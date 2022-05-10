import codecs
codecs.register_error('strict', codecs.ignore_errors)

def read_file(filepath):
    with codecs.open(filepath, 'r', encoding='utf-8', errors='strict') as f:
        return f.read()

def write_file(filepath, data):
    with codecs.open(filepath, 'w', encoding='utf-8', errors='strict') as f:
        f.write(data)

def read_json(filepath):
    with open(filepath) as f:
        return json.load(f)

def write_json(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

def read_yaml(filepath):
    with open(filepath) as f:
        return yaml.load(f)

def write_yaml(filepath, data):
    with open(filepath, 'w') as f:
        yaml.dump(data, f, indent=4)

def read_csv(file
