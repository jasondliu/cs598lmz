import threading
threading.stack_size(67108864)

import sys

sys.path.append("../")

from lib.utils.timer import Timer
from lib.utils.config_parse import cfg_from_file
from lib.utils.logging import setup_logging
from lib.dataset.factory import get_imdb
from lib.dataset.roidb import prepare_roidb, add_bbox_regression_targets
from lib.model.train_val import get_training_roidb, train_net
from lib.model.config import cfg, cfg_from_list, get_output_dir, get_output_tb_dir
from lib.model.bbox_transform import clip_boxes, bbox_transform_inv
from lib.utils.net_utils import save_net, load_net, vis_detections
from lib.utils.blob import im_list_to_blob
from lib.utils.pkl import load_pkl
from lib.utils.pkl import dump_pkl
from lib.utils.pkl import load
