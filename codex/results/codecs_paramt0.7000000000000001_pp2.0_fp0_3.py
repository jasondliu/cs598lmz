import codecs
codecs.register_error('ignore', codecs.ignore_errors)

# TODO: check if to much memory is used
# TODO: implement command line args
# TODO: move calculation of word embeddings in separate file


def get_word_vec(word):
    word = word.lower()
    # print word
    if word in word_vecs:
        return word_vecs[word]
    else:
        return word_vecs["<unk>"]


def get_emoji_vec(emoji):
    if emoji in emoji_vecs:
        return emoji_vecs[emoji]
    else:
        return emoji_vecs["<unk>"]


def get_emoji_vector(emoji1, emoji2):
    vector1 = get_emoji_vec(emoji1)
    vector2 = get_emoji_vec(emoji2)
    vector1 = np.array(vector1)
    vector2 = np.array(vector2)
    vector_sum = vector1 + vector2
    return vector_sum


def get_emoji_sent
