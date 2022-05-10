import codecs
codecs.register_error('strict', codecs.ignore_errors)

def read_file(filename):
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        return f.read()

def write_file(filename, contents):
    with codecs.open(filename, 'w', 'utf-8', 'strict') as f:
        return f.write(contents)

def read_json(filename):
    return json.loads(read_file(filename))

def write_json(filename, data):
    return write_file(filename, json.dumps(data, indent=4, sort_keys=True))

def read_csv(filename):
    with open(filename, 'r') as f:
        return list(csv.reader(f))

def write_csv(filename, data):
    with open(filename, 'w') as f:
        return csv.writer(f).writerows(data)

def read_tsv(filename):
    with open(filename, 'r') as f:
        return list
