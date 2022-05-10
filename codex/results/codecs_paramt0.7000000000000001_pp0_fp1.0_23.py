import codecs
codecs.register_error('ignore', codecs.str_decode_ignore)

def read_corpus(corpus_file):
    data=[]
    for line in corpus_file:
        sentence = line.strip().split(' ')
        data.append(sentence)
    return data

def pad_sentence(sentence, max_length, padding_token=None, PAD_POS=False):
    if len(sentence) > max_length:
        raise Exception("Sentence length exceeds maximum length!")
    new_sentence = sentence[:]
    if PAD_POS:
        new_sentence = ['<s>'] + new_sentence + ['</s>'] 
    if padding_token is not None:
        new_sentence += [padding_token]*(max_length-len(new_sentence))
    return new_sentence


def build_vocab(sentences, min_count=0, max_size=None, lower=False, unk_token='<unk>', 
                pad_token=None, start_token=None,
