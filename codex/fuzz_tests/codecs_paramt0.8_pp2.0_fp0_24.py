import codecs
codecs.register_error("replace_with_space", lambda e: (u" ", e.start + 1))

#This function is based on https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/tutorials/word2vec/word2vec_basic.py
#It reads a tsv file with each line consisting of a sentence, it then tokenizes the
#words, and creates a list of tokens. It then creates a vocab of all the tokens
#that occur in the sentences. This is then used to create a vocabulary of the most
#frequent words.

#This is to a large extent based on this code:
# https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/tutorials/word2vec/word2vec_basic.py

def read_data(filename):
  """Extract the first file enclosed in a zip file as a list of words"""
  with codecs.open(filename, "rb", "utf-8", "replace_with_space") as f:
    data = []
   
