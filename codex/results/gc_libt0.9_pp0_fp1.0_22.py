import gc, weakref
import random
import time
import click
import numpy as np
import pandas as pd
import tracemalloc

from contextlib import closing, contextmanager
from lzma import open as xzopen
from multiprocessing import Value
from pathlib import Path, PosixPath
from typing import Iterable, List, Optional, Tuple
from xml.etree import ElementTree

#pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import

def change_extension(filename: str, ext: str = '') -> str:
    """
    Changes the extension of a file name.

    Parameters
    ----------
    filename : str
        Original file name
    ext : str
        New extension

    Returns
    -------
    str
        The new file name
    """
    prefix, _ = os.path.splitext(filename)
    return prefix + '.' + ext


def normalize(words: List[str]) -> List[str]:
    r"""
    Perform .lower() on words and remove some punctuation.
