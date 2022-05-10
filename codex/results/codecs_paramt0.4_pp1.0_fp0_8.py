import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def read_file(path):
    f = codecs.open(path, 'r', 'utf-8', 'replace_with_space')
    lines = f.readlines()
    f.close()
    return lines

def get_words(lines):
    words = []
    for line in lines:
        words.extend(line.split())
    return words

def get_words_dict(words):
    words_dict = {}
    for word in words:
        if word not in words_dict:
            words_dict[word] = 0
        words_dict[word] += 1
    return words_dict

def get_words_sorted_by_freq(words_dict):
    words_sorted_by_freq = sorted(words_dict.items(), key=lambda x: x[1], reverse=True)
    return words_sorted_by_freq

def get_words_sorted_by_freq_filtered(words_dict, min_fre
