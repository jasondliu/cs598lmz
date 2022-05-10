import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)

import argparse
from copy import copy
import csv
import logging
from math import ceil
import multiprocessing
import os
from random import randrange, shuffle
from sqlalchemy import create_engine, and_, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from textblob import TextBlob
import time
from tqdm import tqdm

from sentietext.utils import get_config, get_class_names
from sentietext.utilities import run_tagger
from sentietext.tagger.individualtagger import IndividualTagger
from sentietext.tagger.mpitagger import MPITagger
from sentietext.tagger.topictagger import TopicTagger
from sentietext.tagger.utils import add_new_notations, update_ann_text, create_and_save
from sentietext.tagger.utils import get_new_annotations,
