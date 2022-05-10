import threading
threading.stack_size(67108864)
import click
import logging
import sys
import os
import time

from pymongo import MongoClient

from . import utils
from . import config
from . import api
from . import tree
from . import data
from . import mining
from . import template
from . import paths
from . import model
from . import web

from .api import get_api
from .template import get_templates
from .data import get_data
from .model import get_model
from .paths import get_paths
from .tree import get_tree
from .mining import get_mining
from .web import get_web

from .config import get_config

# TODO:
# - setup logging
# - setup mongo
# - setup flask
# - setup celery
# - setup and run a task


