import codecs
codecs.register_error('ignore', codecs.ignore_errors)

def get_data(path, file_name):
    file_path = path + '/' + file_name
    if file_name.endswith('.csv'):
        return pd.read_csv(file_path, encoding='utf-8')
    elif file_name.endswith('.xlsx'):
        return pd.read_excel(file_path, encoding='utf-8')
    else:
        raise ValueError('File type not supported')

def get_file_list(path):
    file_list = os.listdir(path)
    return file_list

def get_unique_list(data_list):
    unique_list = list(set(data_list))
    return unique_list

def get_unique_list_from_file(path, file_name):
    data_frame = get_data(path, file_name)
    data_list = data_frame.iloc[:,0].tolist()
    return get_unique_list(data_list
