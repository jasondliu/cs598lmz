import codecs
codecs.register_error('strict', codecs.ignore_errors)

def read_file(file_path):
    """
    Reads a file and returns the contents as a string.
    """
    with open(file_path, 'r') as f:
        return f.read()

def read_file_as_lines(file_path):
    """
    Reads a file and returns the contents as a list of lines.
    """
    with open(file_path, 'r') as f:
        return f.readlines()

def write_file(file_path, content):
    """
    Writes a string to a file.
    """
    with open(file_path, 'w') as f:
        f.write(content)

def write_file_as_lines(file_path, content):
    """
    Writes a list of lines to a file.
    """
    with open(file_path, 'w') as f:
        f.writelines(content)

def read_json(file_path):
    """
    Reads a JSON file
