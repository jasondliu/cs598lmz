import gc, weakref
from functools import partial
import inspect, types
import collections
from collections import defaultdict, namedtuple, OrderedDict
from types import SimpleNamespace
import traceback, sys
from copy import copy, deepcopy
import itertools
import numbers
import json
from contextlib import contextmanager
import subprocess
import pickle
import imp
import re
from io import BytesIO

def _signature_from_callable(c):
    return inspect.signature(c) if inspect.isfunction(c) else inspect.signature(c.__call__)

def _build_arg_dict(c, args, kwargs):
    "Check args, kwargs against the signature of callable c, and return a full dict of arguments"
    #Build a dict of args from fn_args using kwargs,falling back on calling param.default
    s = c if inspect.isfunction(c) else c.__call__ #take the signature from c's actual __call__ method
    arg_dict = dict()
    #Build the args that the callable expects
