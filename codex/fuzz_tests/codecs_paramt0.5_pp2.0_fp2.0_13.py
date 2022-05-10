import codecs
codecs.register_error('strict', codecs.ignore_errors)

# This dictionary maps the integer encoded values to a word
word_dict = {}

# This dictionary maps a word to an integer encoded value
inverse_dict = {}

def get_data():
    """
    Load the training data and return a tuple of training data,
    training labels and vocabulary size
    """
    global word_dict
    global inverse_dict

    # Load the training data
    f = codecs.open("data/train.txt", "r", encoding='utf-8', errors='strict')
    lines = f.readlines()
    f.close()

    # Create the word dictionary
    word_dict = helper.build_dict(lines)
    # Save the word dictionary
    np.save("data/word_dict.npy", word_dict)

    # Encode the files
    encoded_data = [[word_dict[word] for word in helper.tokenize(line)] for line in lines]
    encoded_labels = [helper.get_label_from_filename(filename) for filename in os.list
