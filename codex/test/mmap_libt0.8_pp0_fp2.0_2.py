import mmap
from typing import Dict, Any, List, Tuple
from pathlib import Path
from enum import Enum
import re
from eppy.idfreader import reader
from eppy.bunch_subclass import EpBunch
from eppy.modeleditor import IDF
from . import utility
import numpy as np
from dataclasses import dataclass


@dataclass
class TemplateReference:
    filename: str
    name_patterns: List[str]
    search_pattern: str
