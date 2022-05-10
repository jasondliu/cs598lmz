import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

# import modules & set up logging
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname
 
    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()

sentences = MySentences('/Users/zhaoyang/Documents/Courses/CS224N/Project/data/test') # a memory-friendly iterator
model = gensim.models.Word2Vec(sentences, size=100, window=5, min_count=5, workers=4)

