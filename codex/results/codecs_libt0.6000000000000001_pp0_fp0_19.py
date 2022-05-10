import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

def get_data(file):
    df = pd.read_csv(file, sep=',', encoding='utf-8')
    return df

def get_data_column(file, column):
    df = pd.read_csv(file, sep=',', encoding='utf-8')
    df = df[column]
    return df

def string_split(string, split_num):
    string_list = string.split()
    string_list_chunk = [string_list[i:i + split_num] for i in range(0, len(string_list), split_num)]
    return string_list_chunk

def get_data_column_split(file, column):
    df = pd.read_csv(file, sep=',', encoding='utf-8')
    df = df[column]
    df = df.apply(lambda x: string_split(x, 1))
    return df

def get
