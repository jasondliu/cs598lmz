import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_file_content(filename):
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        return f.read()

def get_file_content_as_list(filename):
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        return f.read().splitlines()

def get_file_content_as_dict(filename):
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        return json.loads(f.read())

def write_file_content(filename, content):
    with codecs.open(filename, 'w', 'utf-8', 'strict') as f:
        f.write(content)

def write_file_content_as_list(filename, content):
    with codecs.open(filename, 'w', 'utf-8', 'strict') as f:
        f.write('\n'.join(content))
