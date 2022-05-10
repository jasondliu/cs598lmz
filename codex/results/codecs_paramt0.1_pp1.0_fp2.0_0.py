import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_data(filename):
    """
    Reads the data from the file and returns a list of lists
    """
    with open(filename, 'r') as f:
        data = f.readlines()
    data = [d.strip().split('\t') for d in data]
    return data

def get_data_dict(filename):
    """
    Reads the data from the file and returns a dictionary
    """
    data = get_data(filename)
    data_dict = {}
    for d in data:
        data_dict[d[0]] = d[1]
    return data_dict

def get_data_dict_list(filename):
    """
    Reads the data from the file and returns a dictionary of lists
    """
    data = get_data(filename)
    data_dict = {}
    for d in data:
        if d[0] not in data_dict:
            data_dict[d[0]] = []
        data_dict[d[0]].append
