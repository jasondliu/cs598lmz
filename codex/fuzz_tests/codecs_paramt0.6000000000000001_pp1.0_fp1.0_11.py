import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def preprocess_string(s):
    # from https://www.kaggle.com/currie32/quora-question-pairs/the-importance-of-cleaning-text
    s = str(s).lower()
    # Special characters
    s = re.sub(r"(\W|\d)", " ", s)
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"\s+[a-zA-Z]\s+", " ", s)
    s = re.sub(r"\^[a-zA-Z]\s+", " ", s)
    s = re.sub(r"\s+", " ", s, flags=re.I)
    s = re.sub(r"^b\s+", "", s)
    return s


