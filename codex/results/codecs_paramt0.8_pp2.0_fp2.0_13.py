import codecs
codecs.register_error('strict', codecs.ignore_errors)

sys.path.append(os.getcwd()+'/../')

from lib.data.babi_data_reader import BABIDataReader
from lib.model.babi_model import BabiModel

from lib.data.dmn_data_reader import DMNDataReader
from lib.model.dmn_model import DMNModel

from lib.data.knowledge_data_reader import KnowledgeDataReader
from lib.model.knowledge_model import KnowledgeModel

from lib.data.lcquad_data_reader import LCQuADDataReader
from lib.model.lcquad_model import LCQuADModel

from lib.data.text_data_reader import TextDataReader
from lib.model.text_model import TextModel

from lib.data.webqa_data_reader import WebQADataReader
from lib.model.webqa_model import WebQAModel

import sqlite3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--dataset', type=str, help
