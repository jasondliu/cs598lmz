import codecs
codecs.register_error('surrogate_escape', codecs.backslashreplace)

def get_content(file_path):
    with codecs.open(file_path, 'r', 'utf-8', 'surrogateescape') as f:
        return f.read()

def get_title(file_path):
    return os.path.splitext(os.path.basename(file_path))[0]


def get_metadata(file_path):
    with codecs.open(file_path, 'r', 'utf-8', 'surrogateescape') as f:
        return f.read().strip()


def get_tags(file_path):
    tags = os.path.splitext(os.path.basename(file_path))[0]
    tags = tags.split('-')[1:]
    return tags


def get_attributes(file_path):
    file_name = os.path.basename(file_path)
    attributes = {}
    for ext in FILE_EXTENSIONS:
        if file_name.endswith
