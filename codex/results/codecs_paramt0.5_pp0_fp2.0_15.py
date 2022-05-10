import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def read_data(filename):
    with codecs.open(filename, encoding='utf-8', errors='replace_with_space') as f:
        data = f.read()
    data = data.lower().replace("<br />", " ")
    return data

def count_words(data):
    data = data.lower()
    data = re.sub(r"[^a-z0-9]+", " ", data)
    data = re.sub(r"[0-9]+", "", data)
    data = data.split()
    return Counter(data)

def main():
    train_pos = os.path.join('data', 'rt-polarity.pos')
    train_neg = os.path.join('data', 'rt-polarity.neg')
    test = os.path.join('data', 'test.txt')
    dev = os.path.join('data', 'dev.txt')

    train_pos_data = read_data(train_pos)
