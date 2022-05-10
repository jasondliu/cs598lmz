import codecs
codecs.set_encoding()

def read_sentence(fname):
    """
    Reads the fname file. Strips the lines and returns
    a list of words.
    File format is:
    1 first_word
    2 second_word

    where 1 is the sentence number and "first_word" is the word
    """
    with codecs.open(fname, 'r', 'utf-8') as f:
        lines = [line.strip().split() for line in f if len(line) > 1]
        sentences, tags = [], []
        for i, line in enumerate(lines):
            if len(line) == 1: # delimiter
                tags.append(i)
        tags.append(len(lines))
        for i in range(1, len(tags)):
            sentences.append(lines[tags[i - 1] + 1:tags[i]])
        return sentences

def posify(sentences):
    """
    POS-tags the sentences.
    Arguments:
        sentences: list of lists, where each sentence
           
