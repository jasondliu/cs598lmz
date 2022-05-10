import weakref

from pylearn2.config import yaml_parse
from pylearn2.gui.patch_viewer import (PatchViewer, make_viewer,
                                      make_viewer_softmax)
from pylearn2.models.dbm import flatten
from pylearn2.expr.nnet import sigmoid_numpy
from pylearn2.utils import consists_of
from pylearn2.utils.string_utils import number_aware_alphabetical_key
from pylearn2.utils import safe_zip
from pylearn2.utils import sharedX
from pylearn2.utils import serial
from pylearn2.utils import wraps

from pylearn2.models.maxout import Maxout
from pylearn2.space import Conv2DSpace
