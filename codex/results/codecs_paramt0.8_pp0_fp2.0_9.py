import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

try:
    import psyco
    psyco.full()
except ImportError:
    print "Not using psyco"

cnn_data_dir = "/u/drspeech/data/TEXT/data/cnn/stories"
data_dir = "/u/drspeech/data/TEXT/data/cnn/cnn_data"

import glob
import os

def clean_line(line):
    return " ".join(line.strip().split())

if __name__ == "__main__":
    for p in glob.glob(os.path.join(cnn_data_dir, "*.story")):
        base = os.path.basename(p)
        base = base.replace(".story", "")
        #print base
        out_p = os.path.join(data_dir, base + ".txt")
        try:
            f = codecs.open(p, "r", "utf-8", "replace_with_space")
            fw
