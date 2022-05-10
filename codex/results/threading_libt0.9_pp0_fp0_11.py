import threading
threading.stack_size(67108864)

import codecs
import csv
import json
import logging
import os
import sys
import traceback
import urllib
import re

from optparse import OptionParser

import yaml

from bisque import BQSession
from bisque.core.celery_app import app
from bisque.core.timer import Timer
from bisque.core.worker_utils import load_config

import bq.util.locks as locks

log = logging.getLogger("bq.update_pipelines")


class UpdatePipelineOptions:
    def __init__(self, config=None, username=None, allowed_projects=None, ignore_projects=None):
        self.username = username
        self.allowed_projects = allowed_projects
        self.ignore_projects = ignore_projects
        self.config = config

    def validate(self):
        if not self.allowed_projects:
            raise Exception("Need to specify at least one allowed project!")


class UpdatePipeline:
    def __init__(self
