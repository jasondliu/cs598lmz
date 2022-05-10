import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

from tqdm import tqdm

from transformers import XLNetConfig, XLNetForSequenceClassification, XLNetTokenizer
from transformers import AdamW
from transformers import glue_compute_metrics as compute_metrics
from transformers import glue_output_modes as output_modes
from transformers import glue_processors as processors
from transformers import set_seed

from sklearn.metrics import precision_recall_fscore_support
from evaluation_metrics import *

from utils import *

logger = logging.getLogger(__name__)

ALL_MODELS = sum((tuple(conf.pretrained_config_archive_map.keys()) for conf in (XLNetConfig,)), ())

MODEL_CLASSES = {
    "xlnet": (XLNetForSequenceClassification, XLNetTokenizer),
}

def predict(args, model, device, evaluate=True):
    eval_output_dir = args.output_dir
