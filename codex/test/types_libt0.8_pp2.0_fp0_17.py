import types
types.ModuleType.__reduce__ = lambda o: (getattr, (o, '__name__'), o)

import abc
import builtins
import contextlib
import enum
import functools
import io
import itertools
import json
import math
import operator
import os
import pathlib
import random
import re
import shlex
import statistics
import string
import sys
import time
import urllib.request
import zipfile
import zlib

class _AOCFileParser:
    def __init__(self, fn_path, to_type=str):
        self.fn_path = fn_path
        self.to_type = to_type
    def __call__(self):
        with open(self.fn_path) as f:
            return [self.to_type(line) for line in f]

class _AOCRaw:
    def __init__(self, *, year, day):
        self.year = year
