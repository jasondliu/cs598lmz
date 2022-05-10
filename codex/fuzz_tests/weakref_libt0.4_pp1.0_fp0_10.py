import weakref

import numpy as np

from . import _pyximport
from . import _utils
from . import _image
from . import _image_utils
from . import _blob
from . import _blob_utils
from . import _segmentation
from . import _segmentation_utils
from . import _tracking
from . import _tracking_utils

_pyximport.install()

from ._utils import *
from ._image import *
from ._image_utils import *
from ._blob import *
from ._blob_utils import *
from ._segmentation import *
from ._segmentation_utils import *
from ._tracking import *
from ._tracking_utils import *


#
# Image
#

class Image(object):
    """
    Image class.

    Attributes
    ----------
    width : int
        Image width.
    height : int
        Image height.
    depth : int
        Image depth.
    num_channels : int
        Number of channels.
    pixel_type : int
        Pixel type.
    """
    def __
