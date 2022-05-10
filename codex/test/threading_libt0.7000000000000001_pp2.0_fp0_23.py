import threading
threading.stack_size(1024*1024*1024)
start = time.time()

def load_raw_data() :
    df = pd.read_csv('data/train.csv', encoding='utf-8')
    df_test = pd.read_csv('data/test.csv', encoding='utf-8')
    return df, df_test

def load_data() :
    return load_raw_data()

def preprocessing_data(df, df_test) :
    print('Data Preprocessing Start')

    df['question1'] = df['question1'].apply(lambda x: str(x))
    df['question2'] = df['question2'].apply(lambda x: str(x))
    df_test['question1'] = df_test['question1'].apply(lambda x: str(x))
    df_test['question2'] = df_test['question2'].apply(lambda x: str(x))

