import codecs
codecs.register_error('replace_with_unknown', lambda e: (' ', e.start + 1))

class Reader:
    def __init__(self, data_dir, word_vocab, tag_vocab, char_vocab, is_train=True, max_iter=None):
        self.max_iter = max_iter
        self.is_train = is_train
        self.data_dir = data_dir
        self.word_vocab = word_vocab
        self.tag_vocab = tag_vocab
        self.char_vocab = char_vocab
        self.unk_word_id = word_vocab['<unk>']
        self.char_eos_id = char_vocab['<eos>']
        self.char_unk_id = char_vocab['<unk>']
        self.word_emb_dim = word_vocab['<emb>'].shape[-1]
        self.char_emb_dim = char_vocab['<emb>'].shape[-1]
        self.tag_emb_dim = tag_
