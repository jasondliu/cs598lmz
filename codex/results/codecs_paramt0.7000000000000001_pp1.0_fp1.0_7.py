import codecs
codecs.register_error('replace_space', lambda e: (u' ','?'))
def read_corpus(file_path):
    data = []
    with codecs.open(file_path, 'r', encoding='utf-8', errors='replace_space') as fin:
        for line in fin:
            words = line.strip().split('\t')
            data.append([int(words[0]),int(words[1])])
    return data

def read_corpus_MIML(file_path):
    data = []
    with codecs.open(file_path, 'r', encoding='utf-8', errors='replace_space') as fin:
        for line in fin:
            line = line.strip().split('\t')
            label = int(line[0])
            words = line[1:]
            data.append([label,words])
    return data

def read_corpus_MIML_test(file_path):
    data = []
    with codecs.open(file_path, 'r', encoding='utf-8', errors='
