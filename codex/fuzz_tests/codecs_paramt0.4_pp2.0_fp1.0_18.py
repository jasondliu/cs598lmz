import codecs
codecs.register_error('strict', codecs.ignore_errors)

def open_utf8(filepath, mode='r'):
    return codecs.open(filepath, mode, 'utf-8', 'strict')

def read_utf8(filepath):
    return open_utf8(filepath).read()

def write_utf8(filepath, contents):
    with open_utf8(filepath, 'w') as f:
        f.write(contents)

def read_json(filepath):
    return json.loads(read_utf8(filepath))

def write_json(filepath, data):
    write_utf8(filepath, json.dumps(data, ensure_ascii=False, indent=2))

def read_yaml(filepath):
    return yaml.load(read_utf8(filepath))

def write_yaml(filepath, data):
    write_utf8(filepath, yaml.dump(data, default_flow_style=False, allow_unicode=True))

def read_csv
