import mmap
import subprocess
import tempfile
import os
import sys
import re
import glob
import shutil
import argparse
import logging
import xml.etree.ElementTree as ET

from collections import defaultdict, OrderedDict

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

from dnachisel import (
    DnaOptimizationProblem,
    random_dna_sequence,
    EnforceGCContent,
    EnforceTranslation,
    EnforceTerminalRestrictionSites,
    EnforceTerminalStickyEnds,
    EnforceTranslationMutability,
    EnforceTm,
    EnforceORF,
    EnforceTranslationOrfMutability,
    EnforceTranslationOrfStability,
    EnforceTranslationOrfCompleteness,
    EnforceTranslationOrf,
    EnforceTranslationOrfMutability,
    EnforceTranslationOrfStability,
    EnforceTranslationOrfCompleteness,
    EnforceTranslationOrfMutability,
    EnforceTranslationOrfSt
