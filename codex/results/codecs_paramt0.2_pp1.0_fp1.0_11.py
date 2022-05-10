import codecs
codecs.register_error('strict', codecs.ignore_errors)

#------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------

def get_file_content(file_name):
    with codecs.open(file_name, 'r', encoding='utf-8', errors='strict') as f:
        return f.read()

def get_file_content_as_list(file_name):
    with codecs.open(file_name, 'r', encoding='utf-8', errors='strict') as f:
        return f.readlines()

def write_file_content(file_name, content):
    with codecs.open(file_name, 'w', encoding='utf-8', errors='strict') as f:
        f.write(content)

def write_file_content_as_list(file_name, content):
    with codecs.open(file_name, 'w', encoding='utf-8', errors='strict') as f:
        f.writelines(content)

#------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------

def get_file_content_as_
