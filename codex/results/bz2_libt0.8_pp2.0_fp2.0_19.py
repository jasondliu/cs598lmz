import bz2
bz2_path = './data/wiki.test.bz2'
output_file = './output/wiki.test.raw'
with open(output_file, 'wb') as out_file, bz2.BZ2File(bz2_path) as bz_file:
    for line in bz_file:
        out_file.write(line)
 
import tqdm
from collections import namedtuple
from gensim.corpora import WikiCorpus

bz2_path = './data/wiki.test.bz2'
text_file = './output/wiki.test.raw'

def bz2_to_text(bz2_path, text_file):
    with open(text_file, 'wb') as out_file, bz2.BZ2File(bz2_path) as bz_file:
        for line in bz_file:
            out_file.write(line)
            
BZ2Wiki = namedtuple('BZ2Wiki', 'bz2_path text_file')

