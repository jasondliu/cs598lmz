import codecs
codecs.register_error("strict", codecs.ignore_errors)

def _read_file(path):
    with codecs.open(path, "r", "utf-8", "ignore") as f:
        return f.readlines()

def _get_raw_data(path):
    return _read_file(path)

def _get_lines(raw_data):
    return [line.split(" ") for line in raw_data]

def _get_words(lines):
    words = []
    for line in lines:
        words.extend(line)
    return words

def _get_word_count(words):
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def _get_sorted_word_count(word_count):
    return sorted(word_count.items(), key=lambda x: x[1], reverse=True)

def _get_vocab_size(
