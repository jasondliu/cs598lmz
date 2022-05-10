import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_file_type(file_name):
    """
    Returns the file type of the given file name.
    """
    if file_name.endswith('.csv'):
        return 'csv'
    elif file_name.endswith('.xls') or file_name.endswith('.xlsx'):
        return 'excel'
    else:
        return 'unknown'

def get_file_name(file_path):
    """
    Returns the file name of the given file path.
    """
    return os.path.basename(file_path)

def get_file_directory(file_path):
    """
    Returns the directory of the given file path.
    """
    return os.path.dirname(file_path)

def get_file_extension(file_path):
    """
    Returns the file extension of the given file path.
    """
    return os.path.splitext(file_path)[1]

def get_file_
