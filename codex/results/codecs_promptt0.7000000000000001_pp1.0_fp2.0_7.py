import codecs
# Test codecs.register_error('replace_with_space',replace_with_space)

import numpy as np
import re

"""
    This script is for generating the data used for training and testing the models.
    
    Training data
    -------------
    The training data is a list of lists of the form
        [[X_1,y_1],[X_2,y_2],...,[X_n,y_n]]
    where X_i is a list of words in a sentence
    and y_i is a list of tags in a sentence
    and n is the number of sentences.
    
    Sentences are given by the lines in the file and are seperated by blank lines.
    
    (add more description here)
    
    Test data
    ---------
    The test data is a list of lists of the form
        [[X_1],[X_2],...,[X_n]]
    where X_i is a list of words in a sentence
    and n is the number of sentences.
    
    Sentences are given by the lines in the file and are seperated by blank lines.
    

