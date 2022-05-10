import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#
#-------------------------------------------------------------------------------

def get_file_content(file_name):
    """
    Read the content of the file and return it
    """
    f = codecs.open(file_name, 'r', 'utf-8', 'strict')
    content = f.read()
    f.close()
    return content

#-------------------------------------------------------------------------------
#
#-------------------------------------------------------------------------------

def get_file_content_as_list(file_name):
    """
    Read the content of the file and return it
    """
    f = codecs.open(file_name, 'r', 'utf-8', 'strict')
    content = f.readlines()
    f.close()
    return content

#-------------------------------------------------------------------------------
#
#-------------------------------------------------------------------------------

def write_file_content(file_name, content):
    """
    Write the content in the file
    """
    f = codecs.open(file_name, 'w', 'utf-8', 'strict')
    f.write(content
