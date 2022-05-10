import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def load_data(path):
    """
    Load dataset
    """
    input_file = os.path.join(path)
    with codecs.open(input_file, "r", encoding='utf-8', errors='replace_with_space') as f:
        data = f.read()

    return data.split('\n')

def preprocess_sentence(w):
    w = w.rstrip().strip()
    
    # creating a space between a word and the punctuation following it
    # eg: "he is a boy." => "he is a boy ."
    # Reference:- https://stackoverflow.com/questions/3645931/python-padding-punctuation-with-white-spaces-keeping-punctuation
    w = re.sub(r"([?.!,¿])", r" \1 ", w)
    w = re.sub(r'[" "]+', " ", w)
    
    # replacing everything with space except (a-z, A-
