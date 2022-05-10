import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

def read_file(filename):
    f = open(filename, 'r', encoding='utf8')
    data = f.read()
    f.close()
    return data

def write_file(filename, data):
    f = open(filename, 'w', encoding='utf8')
    f.write(data)
    f.close()

def read_file_lines(filename):
    f = open(filename, 'r', encoding='utf8')
    lines = f.readlines()
    f.close()
    return lines

def write_file_lines(filename, lines):
    f = open(filename, 'w', encoding='utf8')
    f.writelines(lines)
    f.close()


def read_json_file(filename):
    return json.loads(read_file(filename))

def write_json_file(filename, data):
    write_file(filename, json.dumps(data, indent=
