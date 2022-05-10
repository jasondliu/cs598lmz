import codecs
codecs.register_error('ignore', codecs.ignore_errors)

import networkx as nx
import numpy as np

from pythia.data.dictionaries import Dictionaries as Dic
from pythia.data.knowledge_graph import KnowledgeGraph as KG

class Corpus:
    vocab = []

    def __init__(self, dataset, args):
        # Store unique instance across the the program
        self.dataset = dataset
        self.dicts = Dic(self.dataset, args.use_entity_token)
        self.kg = KG(self.dataset)
        self.args = args
        self.train_dir = os.path.join(self.dataset, args.split, args.input_mode)
        self.valid_dir = os.path.join(self.dataset, "val", args.input_mode)
        self.test_dir = os.path.join(self.dataset, "test", args.input_mode)
        self.vocab_file = os.path.join(self.datas
