import codecs
codecs.register_error('ignore', codecs.lookup('utf-8'))

def generate_dataset(word_dict, type, context_size):
    """
    This function generates a dataset with a given context size, where the center word is the word
    that corresponds to the index of the vector. It generates the context window by taking the index of
    the center word and subtracting the context size.

    :param word_dict: the dictionary of words
    :param type: 'train', 'dev', or 'test'
    :param context_size: the context size to look around each word
    :return: a pandas dataframe with the context window and the corresponding center word
    """

    counter = 0
    data_lst = []
    with open("data/%s.txt" % type, 'r') as f:
        for line in f:
            line = line.strip().split()
            for i in range(len(line)):
                context = []
                for j in range(i - context_size, i + context_size + 1):
                    if j != i:
                        if j >=
