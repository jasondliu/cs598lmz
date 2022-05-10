import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_data():
    '''
    获取数据，返回训练集及测试集
    '''
    with codecs.open('../data/train_set.csv', 'r', 'utf-8', 'ignore') as f:
        reader = csv.reader(f)
        train_set = []
        for line in reader:
            train_set.append(line)
    with codecs.open('../data/test_set.csv', 'r', 'utf-8', 'ignore') as f:
        reader = csv.reader(f)
        test_set = []
        for line in reader:
            test_set.append(line)
    return train_set, test_set

def get_word_dict():
    '''
    获取词典，返回词典及词典长度
    '''
    with
