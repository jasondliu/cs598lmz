import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_text(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def get_words(text):
    return re.findall(r'\w+', text.lower())

def get_word_counts(words):
    return Counter(words)

def get_top_n_words(word_counts, n):
    return word_counts.most_common(n)

def get_word_frequency(word_counts):
    total_count = sum(word_counts.values())
    return {word: count / total_count for word, count in word_counts.items()}

def get_top_n_frequency(word_counts, n):
    return get_top_n_words(get_word_frequency(word_counts), n)

def get_word_probability(word_counts, word):
    return word_counts[word] / sum(word_counts.values
