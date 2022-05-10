import codecs
codecs.register_error('strict', codecs.ignore_errors)

def split_and_pad_sent(sent, max_len, pad=0):
    """
    split and pad a sentence, tokenized with white space
    """
    pad_cnt = max_len - len(sent)
    if pad_cnt <= 0:
        return sent[:max_len]
    return sent + [pad] * pad_cnt


def split_and_pad_sents(text, max_len, pad=0):
    """
    split and pad a list of sentences
    """
    return [split_and_pad_sent(sent, max_len, pad=pad) for sent in text]


def load_train_data(max_src_len, max_tgt_len, min_src_len=1, min_tgt_len=1):
    """
    data format:
    src\t tokens with white space
    tgt\t tokens with white space
    """
    logging.info('reading corpus...')
    with codecs.open(corpus_name,
