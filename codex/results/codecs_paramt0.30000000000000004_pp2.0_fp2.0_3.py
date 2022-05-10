import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_data(filename):
    """
    Reads the data from a file and returns it as a list of lists.
    """
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        data = [line.strip().split('\t') for line in f]
    return data

def get_data_as_dict(filename):
    """
    Reads the data from a file and returns it as a dictionary.
    """
    data = get_data(filename)
    data_dict = {}
    for line in data:
        data_dict[line[0]] = line[1:]
    return data_dict

def get_data_as_dict_of_lists(filename):
    """
    Reads the data from a file and returns it as a dictionary of lists.
    """
    data = get_data(filename)
    data_dict = {}
    for line in data:
        data_dict[line[0]] = line[1:]
    return data
