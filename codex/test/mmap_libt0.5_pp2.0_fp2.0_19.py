import mmap

import numpy as np
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import cv2
from tqdm import tqdm
from torch.utils.data import Dataset

import utils.config as config

from utils.utils import get_all_files_in_dir
from utils.utils import get_all_files_in_dir_recursive
from utils.utils import get_file_name_from_path
from utils.utils import get_file_extension
from utils.utils import get_file_name_without_extension
from utils.utils import get_dir_name_from_path
from utils.utils import get_parent_dir_from_path
from utils.utils import get_file_name_from_path
from utils.utils import get_image_size
from utils.utils import get_all_image_paths_in_dir
from utils.utils import get_all_image_paths_in_dir_recursive
