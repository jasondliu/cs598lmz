import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def print_list(list_data):
    for line in list_data:
        print(line)

def print_list_to_file(list_data, file_name):
    with open(file_name, 'w') as f:
        for line in list_data:
            f.write(line)
            f.write('\n')

def read_file_to_list(file_name):
    list_data = []
    with open(file_name, 'r') as f:
        for line in f:
            list_data.append(line.strip())
    return list_data

def read_file_to_list_with_control(file_name):
    list_data = []
    with open(file_name, 'r') as f:
        for line in f:
            list_data.append(line.strip().replace('\n', ' '))
    return list_data

def read_file_to_list_with_error(file_name
