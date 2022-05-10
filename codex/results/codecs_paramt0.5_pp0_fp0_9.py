import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def normalize_text(text):
    return text.lower().strip().replace("\n", " ").replace("\t", " ").replace("\r", " ").replace(",", " ").replace(".", " ")

def normalize_text_no_punct(text):
    return text.lower().strip().replace("\n", " ").replace("\t", " ").replace("\r", " ").replace(".", " ")

def get_word_counts(text, word_counts):
    for word in text.split(" "):
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1

def get_word_counts_no_punct(text, word_counts):
    for word in text.split(" "):
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts
