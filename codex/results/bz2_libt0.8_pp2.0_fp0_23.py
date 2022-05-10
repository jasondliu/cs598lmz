import bz2
bz2.BZ2File(data_path / 'wikitext-103' / 'wiki.train.tokens', 'r').read(1000)

from nltk.tokenize import word_tokenize

SENTENCE_START = '<s>'
SENTENCE_END = '</s>'

def read_sentences(filename, max_sentences = None, max_tokens = None):
    counter = 0
    total_tokens = 0
    
    sentences = []
    with open(filename) as f:
        for l in f:
            sent = l.strip()
            sent = SENTENCE_START + ' ' + sent + ' ' + SENTENCE_END
            sentences.append(sent)
            counter += 1
            total_tokens += len(sent)
            if counter == max_sentences:
                break
            if max_tokens and (total_tokens > max_tokens):
                break
    return sentences

sentences_wiki_train = read_sentences(data_path / '
