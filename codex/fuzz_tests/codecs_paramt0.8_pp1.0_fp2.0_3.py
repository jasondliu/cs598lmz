import codecs
codecs.register_error('replace_with_space', codecs.replace_with(' '))
with codecs.open('temp_data.txt', 'r', 'utf-8', errors='replace_with_space') as f:
    data = f.read()
    data = data.lower()

    data = text_to_wordlist(data)
    # print(len(data))


def text_to_sentences(text, remove_stopwords=False):
    text = text.split()
    sentences = []
    for i in range(len(text)):
        if text[i] in string.punctuation or text[i] == "\n":
            text[i] = " "
    text = "".join(text)
    text = text.split("\n")
    for line in text:
        sentences.append(line.split())
    if remove_stopwords:
        new_sentences = []
        for sentence in sentences:
            new_sentence = []
            for word in sentence:
                if word not in stopwords.words('english'):
                    new_sent
