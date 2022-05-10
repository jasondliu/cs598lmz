import mmap
import re
import os
from collections import defaultdict
from collections import namedtuple
from collections import OrderedDict
from operator import itemgetter
from operator import attrgetter
from shutil import copyfile
from joblib import Parallel, delayed
from functools import partial

Episodes = namedtuple('Episodes', 'name start finish help')

__all__ = ['pickle_to_file','file_to_pickle','ask_multiple_choice_question','ask_numeric_question','ask_string_question','ask_yesnofalse_question','ask_yesnofalse_question2','ask_yesno_question','ask_yesno_question2','extract_word_from_string','extract_argument_from_string','find_episode_bounds_in_file','create_episode_split_file_name','create_episode_plot_file_name','create_episode_graph_file_name','ensure_dir','write_pickle_file','copy_file','get_episode_from_line_number',
             'get_line_number_from_episode
