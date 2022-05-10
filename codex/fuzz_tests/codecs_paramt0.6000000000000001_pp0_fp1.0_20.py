import codecs
codecs.register_error('replace_with_space', lambda e: (u' ',e.start + 1))

def get_text(filename):
    with codecs.open(filename, "r", encoding='utf-8', errors='replace_with_space') as file:
        text = file.read()
    return text

def get_stopwords():
    with open("stopwords.txt", "r") as file:
        stopwords = file.read().splitlines()
    return stopwords

def get_word_counts(text):
    words = re.findall(r"[\w'-]+", text.lower())
    word_counts = {}
    for word in words:
        if word not in stopwords:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
    return word_counts

def main():
    text = get_text("text.txt")
    stopwords = get_stopwords()
    word_counts = get_word_counts(text)
   
