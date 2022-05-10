import codecs
codecs.register_error('ignore', codecs.lookup('idna'))

#Set logging level
logging.basicConfig(level=logging.INFO)

#Configure logging
logger = logging.getLogger(__name__)

#Define the general purpose global variables
source_file = None
output_file = None

#Define the global variables used to store the data
parent_ids = []
parent_names = []
sub_parent_ids = []
sub_parent_names = []
sub_sub_parent_ids = []
sub_sub_parent_names = []
sub_sub_sub_parent_ids = []
sub_sub_sub_parent_names = []
sub_sub_sub_sub_parent_ids = []
sub_sub_sub_sub_parent_names = []
sub_sub_sub_sub_sub_parent_ids = []
sub_sub_sub_sub_sub_parent_names = []
sub_sub_sub_sub_sub_sub_parent_ids = []
sub_sub_sub_sub_sub_sub_parent_names = []
