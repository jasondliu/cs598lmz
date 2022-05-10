import codecs
codecs.register_error('strict', codecs.ignore_errors)


PICKLE_PATHS = {
    'GE' : 'C:\\Users\\Himel\\Dropbox\\Research\\Harvard-NLP\\Pickles\\ge_v4.pickle',
    'SS' : 'C:\\Users\\Himel\\Dropbox\\Research\\Harvard-NLP\\Pickles\\ss_v4.pickle',
    'AES' : 'C:\\Users\\Himel\\Dropbox\\Research\\Harvard-NLP\\Pickles\\aes_v4.pickle'
}

class Entity(): 
    def __init__(self, typ, name, seg, sec, sen, idx, coref_id=None): 
        self.typ = typ
        self.name = name 
        self.seg = seg
        self.sec = sec
        self.sen = sen
        self.idx = idx
        self.coref_id = coref_id
    def __str__(self):
        return "%-25s%-40s
