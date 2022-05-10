import codecs
codecs.register_error('strict', codecs.ignore_errors)

# TODO: rewrite the code below to be more pythonic

def __init_file(file_name):
    with open(file_name, 'w') as f:
        f.write('')

def __is_file_empty(file_name):
    with open(file_name, 'r') as f:
        content = f.read()
        return content == ''

def __add_entry_to_file(file_name, entry):
    with open(file_name, 'a') as f:
        f.write(entry)

def __get_entries_from_file(file_name):
    with open(file_name, 'r') as f:
        content = f.read()
        return content.splitlines()

def __get_all_entries_from_file(file_name):
    return __get_entries_from_file(file_name)

def __remove_entry_from_file(file_name, entry):
    entries = __get_entries
