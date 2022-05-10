import codecs
codecs.register_error('strict', codecs.ignore_errors)

# local imports
from utils.arg_parser import ArgParser
from utils.utils import create_dirs, get_file_name
from utils.utils import is_valid_file, is_valid_dir, is_valid_url
from utils.url_utils import download_url
from utils.data_utils import *
from utils.ltf_utils import read_ltf
from utils.kaf_utils import parse_kaf
from utils.json_utils import write_json
from utils.term_utils import *
from utils.edl_utils import is_linked_term, write_edl_results

# program name
PROGRAM_NAME = 'link-ner'

# program version
PROGRAM_VERSION = '1.0.0'


# define the Pipeline class to perform linking
class Pipeline:

    # initialize
    def __init__(self, args):
        # set the data directory
        self.data_dir = args.data_dir
        # set the input directory
       
