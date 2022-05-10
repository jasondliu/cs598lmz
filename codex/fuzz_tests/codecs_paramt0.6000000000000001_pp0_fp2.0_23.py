import codecs
codecs.register_error('strict', codecs.ignore_errors)

#---------------------------------------------------------------------------------------------------

# Module-level variables

#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------

def get_file_object(file_name, mode, encoding='utf-8', errors='strict'):
    """
    Open a file and return a file object, or None if there was a problem.
    """
    try:
        file_object = codecs.open(file_name, mode, encoding, errors)
    except IOError:
        file_object = None
    return file_object

#---------------------------------------------------------------------------------------------------

def read_file(file_name, encoding='utf-8', errors='strict'):
    """
    Open a file, read it, and return the contents, or None if there was a problem.
    """
    file_object = get_file_object(file_name, 'r', encoding, errors)
    if file_object is not None:
        file_contents = file_object.read()
        file_object.close()
    else:
        file_contents = None

