import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def load_data(path, max_sent_length, max_doc_length):
  '''
  Loads the data.
  '''
  sentences = []
  docs = []
  file = codecs.open(path, 'r', 'utf-8', errors='replace_with_space')
  for line in file:
    line = line.replace("\n","")
    line = line.replace("\r","")
    line = line.replace("<"," ")
    line = line.replace(">"," ")
    line = line.replace("/"," ")
    line = line.replace("*"," ")
    line = line.replace("\""," ")
    line = line.replace("\\"," ")
    line = line.replace("\t"," ")
    line = line.replace("@"," ")
    line = line.replace("+"," ")
    line = line.replace("."," ")
    line = line.replace("-"," ")
    line =
