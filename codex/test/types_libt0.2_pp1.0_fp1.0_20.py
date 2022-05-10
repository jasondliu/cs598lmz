import types
types.ModuleType.__getattribute__ = types.ModuleType.__getattr__

import sys
import os
import re
import logging
import argparse
import subprocess
import shutil
import tempfile
import json
import time
import datetime
import copy
import glob
import math
import random
import string
import hashlib
import uuid
import traceback
import collections
import multiprocessing
from multiprocessing import Process, Queue, Pool
from multiprocessing.pool import ThreadPool
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing.dummy import Process as ThreadProcess
from multiprocessing.dummy import Queue as ThreadQueue
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing.dummy import Process as ThreadProcess
