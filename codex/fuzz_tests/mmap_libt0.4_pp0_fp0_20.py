import mmap
import os
import re
import subprocess
import sys
import time
import traceback

import numpy as np
import tensorflow as tf

from tensorflow.python.client import timeline
from tensorflow.python.framework import meta_graph
from tensorflow.python.framework import ops
from tensorflow.python.ops import data_flow_ops
from tensorflow.python.ops import variables
from tensorflow.python.platform import gfile
from tensorflow.python.platform import tf_logging as logging
from tensorflow.python.training import coordinator
from tensorflow.python.training import queue_runner
from tensorflow.python.training import saver as tf_saver
from tensorflow.python.training import session_manager
from tensorflow.python.training import supervisor
from tensorflow.python.training import training_util
from tensorflow.python.training import device_setter

from tensorflow.python.training.saver import Saver
from tensorflow.python.training.saver import _SaverRestoreOperation
from tensor
