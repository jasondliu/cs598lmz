import selectors
import sys
import time
import datetime

from collections import namedtuple
#from multiprocessing import Process
from multiprocessing import Queue, Event
from queue import Empty

import cv2
from PIL import Image

from . import common
from . import config
from . import debug
from . import detector
from . import model
from . import visualizer
from . import utils
from . import tracking
from . import workers

from .utils import *
from .config import *
from .debug import *
from .common import *
from .workers import *

from .detector import Detector
from .visualizer import Visualizer
from .model import Model
from .tracking import Tracker

def main(args):

    # Initialize Model
    model = Model()

    # Initialize Detector
    detector = Detector()

    # Initialize Visualizer
    visualizer = Visualizer()

    # Initialize Tracker
    tracker = Tracker(detector, visualizer, model)

    # Create Queues
    input_queue = Queue(maxsize=1)
    output
