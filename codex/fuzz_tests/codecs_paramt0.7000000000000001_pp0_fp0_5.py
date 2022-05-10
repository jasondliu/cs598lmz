import codecs
codecs.register_error('replace_with_space', codecs.lookup('utf-8'), lambda e: (u' ', e.start + 1))
def remove_punctuation(s):
    return re.sub(ur"([\u4e00-\u9fa5])*\p{P}*([\u4e00-\u9fa5])*", "", s)

def remove_numbers(s):
    return re.sub(ur'[\d]*', "", s)

def remove_english_words(s):
    return re.sub(ur'[A-Za-z]*', "", s)

def remove_chinese_numbers(s):
    return re.sub(ur'[零一二两三四五六七八九十百千万亿兆]*', "", s)

def naive_tokenize(sentence):
    """Tokenize a sentence using a naive approach."""
    return [remove_punctuation(token) for token in re.split(
