import codecs
codecs.register_error("strict", codecs.ignore_errors)

# Global counters
g_num_of_sentences = 0
g_num_of_words = 0
g_num_of_one_word_sentences = 0
g_num_of_two_word_sentences = 0
g_num_of_three_word_sentences = 0
g_num_of_four_word_sentences = 0
g_num_of_long_sentences = 0
g_longest_sentence = ""
g_longest_sentence_len = 0
g_num_of_short_sentences = 0
g_shortest_sentence = ""
g_shortest_sentence_len = 0
g_avg_sentence_length = 0
g_avg_word_length = 0
g_num_of_words_of_length_1 = 0
g_num_of_words_of_length_2 = 0
g_num_of_words_of_length_3 = 0
g_num_of_words_of_length_4 = 0
g
