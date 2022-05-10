import weakref

import numpy as np

from skimage.measure import label, regionprops

from .base_detector import BaseDetector
from .mrcnn import utils

logger = logging.getLogger(__name__)


# from https://gist.github.com/wllhf/a4533e0adebe57e3ed06d4b50c8419ae
def rle_encode(mask):
    """Encodes a mask in Run Length Encoding (RLE).
    Returns a string of space-separated values.
    """
    assert mask.ndim == 2, "Mask must be of shape [Height, Width]"
    # Flatten it column wise
    m = mask.T.flatten()
    # Compute gradient. Equals 1 or -1 at transition points
    g = np.diff(np.concatenate([[0], m, [0]]), n=1)
    # 1-based indicies of transition points (where gradient != 0)
