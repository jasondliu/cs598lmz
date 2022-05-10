import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

# Get text from files and make a corpus
def make_corpus(folder):
  corp = []                                                               # define a list
  for f in os.listdir(folder):                                            # for every file in this folder
    with open(folder + "/" + f, errors='replace_with_space') as fin:      # open the file
      text = fin.read()                                                   # read everything in it
      text = text.replace('\n', ' ')                                      # replace newlines (aka hard returns) with spaces
      corp.append(text)                                                   # add to the corpus
  return corp                                                             # return the corpus

# Given a corpus, find the most frequent words
def find_freq(corp):
  freq = {}
  for text in corp:                                                       # for every text in the corpus
    for word in text.split():                                             # for every word in the text
      if len(word) > 3:                                                   # as long as it's longer than
