import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

#reload(sys)
#sys.setdefaultencoding('utf-8')

def get_word_freq(path):
    word_freq = {}
    with open(path) as f:
        for line in f:
            line = line.decode('utf-8').strip().split('\t')
            word = line[0]
            freq = int(line[1])
            word_freq[word] = freq
    return word_freq

def get_word_freq_dict(path):
    word_freq = {}
    with open(path) as f:
        for line in f:
            line = line.decode('utf-8').strip().split('\t')
            word = line[0]
            freq = int(line[1])
            word_freq[word] = freq
    return word_freq

def get_word_freq_list(path):
    word_freq_list = []
    with
