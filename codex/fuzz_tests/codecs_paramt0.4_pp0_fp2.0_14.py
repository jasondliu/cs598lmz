import codecs
codecs.register_error('strict', codecs.ignore_errors)


def get_content(file_name):
    """
    Read the file and return the content.
    """
    with codecs.open(file_name, 'r', encoding='utf-8') as f:
        return f.read()


def get_data(file_name):
    """
    Read the file and return the data.
    """
    with open(file_name, 'rb') as f:
        return f.read()


def write_content(file_name, content):
    """
    Write the content in the file.
    """
    with codecs.open(file_name, 'w', encoding='utf-8') as f:
        f.write(content)


def write_data(file_name, data):
    """
    Write the data in the file.
    """
    with open(file_name, 'wb') as f:
        f.write(data)


def get_files(path, recursive=False, exclude=None):
    """
    Return all files in the
