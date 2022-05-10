import codecs
codecs.open
import string
import os

def load_data(data_dir):
    data_file = os.path.join(data_dir, "illinois.txt")
    if not os.path.exists(data_file):
        print("Data file %s not found." % data_file)
    with open(data_file, "r") as f:
        return f.read()

def preprocess_text(text):
    text = text.lower()
    text = text.replace(".", " .")
    words = text.split()

    word_to_id = {}
    id_to_word = {}
    for word in words:
        if word not in word_to_id:
            new_id = len(word_to_id)
            word_to_id[word] = new_id
            id_to_word[new_id] = word

    corpus = np.array([word_to_id[w] for w in words])

    return corpus, word_to_id, id_to_word

def create_co_
