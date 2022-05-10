import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

# 从文件中获取数据
def get_data_from_file(file_name):
    data = []
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(line.strip())
    return data

# 从文件中获取数据
def get_data_from_file_with_id(file_name):
    data = []
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(line.strip().split('\t'))
    return data

# 从文件中获取数据
def get_data_from_file_with_id_and_label(file_name):
    data = []
    with open(file_
