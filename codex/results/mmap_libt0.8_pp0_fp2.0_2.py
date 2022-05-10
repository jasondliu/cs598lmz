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
    replace_pattern: str
    default_parameters: Dict[str, Any]
    idf: IDF
    
    def __post_init__(self):
        self.idf = IDF(self.filename, ep_version="9.0")
        self.default_parameters = self.parse_default_parameters()


    @staticmethod
    def get_default_parameter(obj: Dict[str, Any]) -> Any:
        """
        Returns the default value of an object, i.e. the value of the second
        field of the object
        """

