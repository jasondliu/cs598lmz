import codecs
codecs.register_error('strict', codecs.ignore_errors)

data_path = 'data'

def get_train_data(data_path):
    """
    load train data from csv file
    """
    train_data = pd.read_csv(os.path.join(data_path,'train_set.csv'))
    train_data = train_data.dropna(axis=0)
    train_data['words'] = train_data['words'].apply(lambda x: x.split(' '))
    train_data['words_len'] = train_data['words'].apply(lambda x: len(x))
    train_data = train_data[train_data['words_len']>=5]
    train_data = train_data.reset_index(drop=True)
    return train_data

def get_test_data(data_path):
    """
    load test data from csv file
    """
    test_data = pd.read_csv(os.path.join(data_path,'test_set.csv'))
    test
