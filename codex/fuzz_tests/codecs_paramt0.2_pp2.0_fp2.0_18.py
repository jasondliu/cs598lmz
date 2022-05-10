import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_file_path(file_name):
    return os.path.join(os.path.dirname(__file__), file_name)

def get_file_content(file_name):
    with codecs.open(get_file_path(file_name), 'r', 'utf-8', 'strict') as f:
        return f.read()

def get_file_content_as_lines(file_name):
    return get_file_content(file_name).splitlines()

def get_file_content_as_json(file_name):
    return json.loads(get_file_content(file_name))

def get_file_content_as_csv(file_name):
    return csv.DictReader(get_file_content_as_lines(file_name))

def get_file_content_as_csv_with_header(file_name):
    return csv.DictReader(get_file_content_as_lines(file_name), fieldnames
