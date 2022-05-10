import mmap
import sys
import struct
import time
import os
import numpy as np
import pandas as pd
import datetime
import warnings
warnings.filterwarnings('ignore')

from multiprocessing import Process, Queue
from threading import Thread
from queue import Empty

from os import path, pardir
main_dir = path.abspath(path.dirname(sys.argv[0]))  # Dir of main
sys.path.append(main_dir)
sys.path.append(main_dir + "/" + pardir)

from classes.channel import Channel
from classes.channel_group import ChannelGroup
from classes.channel_group_collection import ChannelGroupCollection
from classes.channel_collection import ChannelCollection
from classes.file_manager import FileManager
from classes.file_writer import FileWriter
from classes.file_reader import FileReader
from classes.data_reader import DataReader
from classes.data_writer import DataWriter
from classes.data_manager import DataManager
from classes.data_processor import DataProcessor
from classes.data_plotter import DataPlotter
