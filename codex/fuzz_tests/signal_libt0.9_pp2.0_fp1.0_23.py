import signal
signal.signal(signal.SIGINT, signal_handler)

# the number of words to look ahead to calculate
# the probability that the virtual assistant should answer or not
LOOKAHEAD_WORDS = 10
# the maximum value the probability can have
# the higher, the more likely it is to respond
MAX_PROBA = 0.66

def probability_of_responding_to_message(text):
    # I am using mean_sentence_length for now
    # it can be more sophisticated using other metrics
    # like words per sentence
    # or lexical density
    mean_sentence_length = 0
    sentences = tokenize.sent_tokenize(text)
    for sentence in sentences:
        word_count = len(word_tokenize(sentence))
        mean_sentence_length += word_count
    mean_sentence_length /= len(sentences)
    probability_of_responding = float(mean_sentence_length)/LOOKAHEAD_WORDS
    if (probability_of_responding > MAX_PROBA):
        return MAX
