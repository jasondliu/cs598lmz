import codecs
codecs.register_error('strict', codecs.ignore_errors)  # ignore error
nltk.data.path.append('./data')
sys.path.append('../..')

from lib.helpers import load_config, load_english_stopwords, get_all_question_types, stringify_question_type_list, logger
from lib.utils import get_qts_from_qtp_string, print_stats
from lib.golden_graph import GoldenGraph, GoldenNode
from lib.CandidateGraph import CandidateGraph


use_golden_nodes = False
use_golden_node_types = True
use_golden_node_words_lemmatize = False
use_golden_node_words = False
use_golden_node_idfs = False

use_candidate_nodes = False
use_candidate_node_types = True
use_candidate_node_words_lemmatize = False
use_candidate_node_words = False
use_candidate_node_idfs = False

use_candidate_graph_edges =
