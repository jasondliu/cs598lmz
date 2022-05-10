import bz2
bz2.__file__

import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')

from config import args

config = {
    "processes": args.n_threads,
    "pages_per_part": 20000,
    "strict_xml": False,
    "parts": args.parts,
    "parallel_init": True,
    "base_file": args.base_file,
    "reader": "wikicorpus",
    "parallel_processing": True,
    "neighbouring_pages": True,
    "file_name": args.mapping_file,
    "extension": ".bz2",
    "absolute_offsets": True,
    "flush_freq": 25,
    "compression": 'bz2',
}


if args.mapping_file == 'databases/enwiki-20170920-pages-articles-multistream.xml-p27294790p30185318.txt.bz2':

