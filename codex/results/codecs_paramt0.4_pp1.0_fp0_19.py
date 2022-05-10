import codecs
codecs.register_error('ignore', codecs.ignore_errors)

# from utils.data_utils import *
import utils.data_utils as data_utils
from utils.data_utils import *

from utils.config_utils import get_model_args
from utils.config_utils import process_config
from utils.config_utils import get_config_from_json
from utils.dirs import create_dirs
from utils.logger import LoggerN
from utils.utils import get_args
from utils.utils import save_dict_to_json
from utils.utils import load_dict_from_json
from utils.utils import get_timestamp
from utils.utils import get_timestamp_dir
from utils.utils import get_timestamp_dir_from_dict

from models.cnn_models import *
from models.rnn_models import *
from models.cnn_rnn_models import *
from models.cnn_rnn_models import *
from models.cnn_rnn_models import *
from models.cnn_
