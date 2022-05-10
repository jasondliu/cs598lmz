import codecs
codecs.register_error('strict', codecs.ignore_errors)

def read_file(filename):
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        return f.read()

def write_file(filename, contents):
    with codecs.open(filename, 'w', 'utf-8', 'strict') as f:
        f.write(contents)

def read_json(filename):
    return json.loads(read_file(filename))

def write_json(filename, contents):
    write_file(filename, json.dumps(contents, indent=4))

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        return [row for row in reader]

def write_csv(filename, rows):
    with open(filename, 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

def read_tsv(filename):
    with open(filename, 'rb
