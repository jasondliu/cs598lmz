import codecs
codecs.getwriter('utf-8')(sys.stdout)

def main(sentence_file, label_file, svm_file):
    labels = dict()
    sentences = dict()
    svm_out = dict()
    for line in codecs.open(label_file, 'r', 'utf-8'):
        line = line.strip().split(' ')
        label = line[0]
        id = line[1]
        labels[id] = label
    for line in codecs.open(sentence_file, 'r', 'utf-8'):
        line = line.strip().split(' ')
        label = line[0]
        id = line[1]
        sentence = ' '.join(line[2:])
        sentences[id] = sentence
    for line in codecs.open(svm_file, 'r', 'utf-8'):
        line = line.strip().split('\t')
        id = line[0]
        if id not in svm_out:
            svm_out[id] = dict()

