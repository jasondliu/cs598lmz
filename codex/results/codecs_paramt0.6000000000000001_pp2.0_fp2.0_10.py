import codecs
codecs.register_error("replace_with_space",replace_with_space)

def read_file(filename):
    f = codecs.open(filename, encoding='utf-8', errors='replace_with_space')
    x_text = f.read()
    x_text = x_text.lower()
    f.close()
    return x_text

def clean_str(string):
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
    string
