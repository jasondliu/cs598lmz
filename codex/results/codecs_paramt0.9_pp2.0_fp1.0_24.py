import codecs
codecs.register_error('strict', codecs.ignore_errors)
detokenizer = nltk.TreebankWordDetokenizer().detokenize
def detokenize(text, replace_w=False):
    if replace_w:
        patterns = [(re.compile(r'\s+(w)\s+'), r'%s ' % 'w'),
                         (re.compile(r'\s+(\d+)\s+'), r'%s ' % '#')]
        for p, r in patterns:
            text = p.sub(r, text)

    return detokenizer(nltk.word_tokenize(text))

class Tokenizer:
    def __init__(self):
        self.word_dict = {}
        self.word_dict_r = []
        self.word_freq = {}
        self.max_len = 0
        self.num_words = 0
        self.word_dict['<pad>'] = PAD_ID
        self.word_dict['<go>'] = GO_ID
        self.word_dict['<eos
