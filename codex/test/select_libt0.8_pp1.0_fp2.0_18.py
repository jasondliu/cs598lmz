import select
import sys
import time
import threading
import math

import numpy as np

# If you have problems with pylibftdi, you may need to reinstall it
# from the master branch.

import pylibftdi

from tatsu.ast import AST

from pybtex.database import BibliographyData
from pybtex.database.input.bibtex import Parser

from pybtex.style import Names
from pybtex.style.template import (
    join, words, first_of, field, optional, first_of, sentence, words)
from pybtex.style.formatting.plain import Style as PlainStyle
from pybtex.style.formatting.unsrt import Style as UnsrtStyle

# TODO: Store types of references
# TODO: Cache formatted references

STYLES = {
    'plain': PlainStyle,
    'unsrt': UnsrtStyle,
}

def format_bib(style, entries):
    bib = BibliographyData()

