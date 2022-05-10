import bz2
bz2.BZ2File(path)

#3. If we can use .gz or .bz2 files in a text-mode with a compression library, we can also do this for pickled objects. 
#   This could be useful if we want to send someone a pickled binary blob and don’t want to make the file too big,
#   or if we want to stream data to and from a network socket.

#   To do this, we simply open the file in binary mode and wrap it with a BZ2 or Gzip instance.

#   To illustrate, let’s make a pickled data structure with three variables:
import pickle
data = {
    'a': [1, 2.0, 3, 4+6j],
    'b': ("character string", b"byte string"),
    'c': {None, True, False}
}

#   To pickle the data, we must first open a binary file for writing:

with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)

#   If we examine the contents
