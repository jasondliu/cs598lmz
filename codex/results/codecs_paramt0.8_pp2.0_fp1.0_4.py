import codecs
codecs.register_error('Ignore', codecs.lookup_error('ignore'))

def read_sentences_from_file(fname):
    sentences = []
    sent = []
    # For each line in the input file
    for i, line in enumerate(codecs.open(fname, 'r', 'utf-8', 'Ignore')): 
        line = re.sub("\s+", " ", line).strip()
        if not line:
            if sent:
                sentences.append(sent)
                sent = []
            continue
        fields = line.split(' ')
        assert len(fields)==4
        sent.append(fields)
    if sent:
        sentences.append(sent)
    print "Read " + str(len(sentences)) + " sentences from " + fname
    return sentences

def read_sentences_from_stdin():
    sentences = []
    sent = []
    # For each line in the input file
    for i, line in enumerate(sys.stdin): 
        line = re.sub("\s+", "
