import mmap
import os
import re
import sys
import time
from datetime import datetime
from glob import glob
from os.path import join
from pathlib import Path
from typing import List, Optional, Tuple

import click
import numpy as np
from tqdm import tqdm

from . import __version__
from . import utils
from . import video
from .config import Config
from .config import ConfigError
from .config import ConfigMissingError
from .config import ConfigNotFoundError
from .config import ConfigNotValidError
from .config import ConfigValueError
from .config import get_config
from .config import get_default_config
from .config import get_default_config_path
from .config import get_default_config_path_from_env
from .config import get_default_config_path_from_home
from .config import get_default_config_path_from_xdg_config_home
from .config import get_default_config_path_from_xdg_config_home_or_home
from .config import get_default_config_path_from_
