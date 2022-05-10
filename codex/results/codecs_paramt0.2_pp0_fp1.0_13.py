import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_data(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return data

def get_data_as_list(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
    return data

def get_data_as_list_of_lists(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
    data = [line.split() for line in data]
    return data

def get_data_as_list_of_lists_of_lists(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
    data = [line.split() for line in data]
    data = [[int(i) for i in line] for line in data]
    return data

def get_data_as_list_of_lists_of_lists_of_lists(filename):
    with open(filename, 'r')
