import codecs
codecs.register_error('strict', codecs.ignore_errors)

#
# Helper functions.
#

def parse_input(input):
    """Parses the input file into a list of (word, tag) tuples."""
    tagged_sentences = []
    sentence = []
    for line in input:
        line = line.strip()
        if line == "":
            if sentence:
                tagged_sentences.append(sentence)
                sentence = []
        else:
            word, tag = line.split("\t")
            sentence.append((word, tag))
    if sentence:
        tagged_sentences.append(sentence)
    return tagged_sentences

def parse_test_input(input):
    """Parses the input file into a list of words."""
    sentences = []
    sentence = []
    for line in input:
        line = line.strip()
        if line == "":
            if sentence:
                sentences.append(sentence)
                sentence = []
        else:
            word = line
            sentence.append(word)
