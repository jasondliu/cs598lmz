import codecs
codecs.register_error('replace_with_space', lambda e: (u' ',e.start + 1))

def gzip_decompress(file_path):
    """
    Decompress a .gz file, returns the uncompressed file's name.
    """
    in_file = gzip.open(file_path, 'rb')
    out_file = os.path.splitext(file_path)[0]
    with open(out_file, 'wb') as f:
        f.write(in_file.read())
    in_file.close()
    return out_file


def tokenize(sentence):
    """
    Tokenize a sentence with English tokenizer.
    """
    return [x.strip() for x in nltk.word_tokenize(sentence)]


def parse_sentence(sentence):
    """
    Parse a sentence with Standford Parser.
    """
    return list(stanford.parse(sentence))


def sentence_to_dependencies(sentence):
    """
    Parse a sentence and return a list of dependencies
