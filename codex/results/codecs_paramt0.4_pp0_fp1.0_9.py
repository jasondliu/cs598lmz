import codecs
codecs.register_error('surrogate_escape', codecs.backslashreplace)

def read_file(filename):
    with codecs.open(filename, encoding='utf-8', errors='surrogateescape') as f:
        return f.read()

def write_file(filename, data):
    with codecs.open(filename, 'w', encoding='utf-8', errors='surrogateescape') as f:
        f.write(data)

def read_json(filename):
    return json.loads(read_file(filename))

def write_json(filename, data):
    write_file(filename, json.dumps(data, indent=2, sort_keys=True))

def read_csv(filename):
    with open(filename, 'r') as f:
        return list(csv.DictReader(f))

def write_csv(filename, data):
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writer
