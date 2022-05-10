import weakref

import numpy as np

from .. import config
from .. import utils
from .. import _utils
from .. import data
from .. import paths
from .. import exceptions
from .. import events

from . import _base

import logging
logger = logging.getLogger(__name__)


class Dataset(_base.Dataset):
    """
    Dataset class for the CIFAR-10 dataset.

    This class inherits from :class:`~torchdata.Dataset`.

    **Parameters:**

    - **path** (string) - Path to the dataset.
    - **download** (bool) - If ``True``, downloads the dataset from the internet and
      puts it in root directory. If dataset is already downloaded, it is not
      downloaded again.
    - **transform** (callable, optional) - A function/transform that  takes in an PIL image
      and returns a transformed version. E.g, ``transforms.RandomCrop``
    - **target_transform** (callable, optional) - A function/transform that takes in the

