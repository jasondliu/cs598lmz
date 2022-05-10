import codecs
codecs.register_error('replace_with_space', lambda e: (u' ',e.start + 1))

def get_data(path):
    data = []
    with codecs.open(path, 'r', 'utf-8', 'replace_with_space') as f:
        for line in f:
            data.append(line.strip())
    return data

def get_alphabet_dict(alphabet):
    alphabet_dict = {}
    for i, char in enumerate(alphabet):
        alphabet_dict[char] = i + 1
    return alphabet_dict

def get_tags(tags_path):
    tags = []
    with codecs.open(tags_path, 'r', 'utf-8', 'replace_with_space') as f:
        for line in f:
            tags.append(line.strip())
    return tags

def get_tags_dict(tags):
    tags_dict = {}
    for i, tag in enumerate(tags):
        tags_dict[tag] = i
    return tags_dict

def create_dataset(
