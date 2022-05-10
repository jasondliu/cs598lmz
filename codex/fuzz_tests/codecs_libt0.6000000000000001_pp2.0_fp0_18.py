import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

def get_data(file_path):
    df = pd.read_csv(file_path, encoding='utf-8')
    return df

def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

def get_stop_words(stop_word_path):
    stop_word_file = open(stop_word_path, 'r', encoding='utf-8')
    stop_words = [line.strip() for line in stop_word_file.readlines()]
    return stop_words

def get_embedding(embedding_path):
    embedding_file = open(embedding_path, 'r', encoding='utf-8')
    embedding_dict = {}
    for line in embedding_file.readlines():
        values = line.split()
        word =
