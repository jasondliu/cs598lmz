import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def read_vocab(vocab_path):
    with codecs.open(vocab_path, 'r', 'utf-8', 'replace_with_space') as f:
        words = [line.strip() for line in f]
    word_to_id = {k: v for (k, v) in zip(words, range(len(words)))}
    return words, word_to_id

def read_category():
    categories = ['体育', '财经', '房产', '家居', '教育', '科技', '时尚', '时政', '游戏', '娱乐']
    cat_to_id = dict(zip(categories, range(len(categories))))
    return categories, cat_to_id

def to_words(content, words):
    return ''.join(words[x] for x in content)

def
