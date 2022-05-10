import mmap
import sys
import mmap_ext
from collections import defaultdict

def one_sentence_per_line(fn, outfn):
    data = open(fn).read()
    data = re.sub("\n+","\n",data)
    data = re.sub("\r+","\r",data)
    data = re.sub("\r\n+","\r\n",data)
    data = re.sub("\n+\r","\r",data)
    data = data.replace("\r","\n")
    data = re.sub("\n+","\n",data)
    
    with open(outfn, 'w') as f:
        f.write(data)

def dict_to_kv_file(d, fn):
    with open(fn, 'w') as f:
        for k in d:
            f.write(k + "\t" + ",".join(d[k]) + "\n")

def get_sentence_lengths(fn, outfn):
    sentence_lengths =
