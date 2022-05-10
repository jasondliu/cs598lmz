import weakref

import numpy as np

from .base import Base
from .utils import get_logger

logger = get_logger(__name__)


class BaseDataset(Base):
    def __init__(self, config):
        super().__init__(config)
        self.config = config
        self.data_dir = config.data_dir
        self.data_type = config.data_type
        self.data_name = config.data_name
        self.data_path = os.path.join(self.data_dir, self.data_name)
        self.data_ext = config.data_ext
        self.data_file = self.data_name + self.data_ext
        self.data_path_file = os.path.join(self.data_dir, self.data_file)
        self.data_path_file_gz = self.data_path_file + '.gz'
        self.data_path_file_bz2 = self.data_path_file + '.bz2'
        self.data
