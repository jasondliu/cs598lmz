import codecs
codecs.register_error("strict", codecs.ignore_errors)

import string



# import os
# import sys

# sys.path.append(os.getcwd())
# sys.path.append("../")
# import SubWords.Word
# import SubWords.Sentence
import List.List


class RuSentRelParser(object):
    def __init__(self,
                 rusentrel_file_path,
                 rusentrel_expanded_file_path,
                 rusentrel_expanded_file_path_validation,
                 rusentrel_expanded_file_path_test,
                 existing_words_vocab_path,
                 min_word_freq,
                 replace_dig_with_num,
                 pad_to_max_len_v2,
                 label_to_num_mapping,
                 num_to_label_mapping,
                 word_to_num_v2_mapping,
                 num_to_word_v2_mapping,
                 word_to_num_v1_mapping,
                
