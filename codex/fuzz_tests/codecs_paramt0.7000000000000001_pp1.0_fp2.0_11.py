import codecs
codecs.register_error('skip', lambda _: u'\N{REPLACEMENT CHARACTER}')

def log_message(message):
    sys.stdout.write(message)
    sys.stdout.write('\n')
    sys.stdout.flush()

def get_data(file_name):
    file_handle = open(file_name, mode='r')
    lines = file_handle.readlines()
    return lines

def get_input_data():
    i = 0
    lines = get_data(input_file_name)
    for line in lines:
        if(i == 0):
            num_of_templates = int(line)
        elif(i == 1):
            num_of_queries = int(line)
        elif(i == 2):
            template_list = line.split()
        elif(i == 3):
            query_list = line.split()
        i = i + 1
    return num_of_templates, num_of_queries, template_list, query_list

def get_s
