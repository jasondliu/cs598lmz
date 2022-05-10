import threading
threading.stack_size(32768)
import os
import sys
moduleDir = os.path.dirname(__file__)
sys.path.append(moduleDir)
from bwgCommon import *
from bx.intervals.io import GenomicIntervalReader
from py_scripts import psl_to_bed
from py_scripts.maf_to_bed import MafToBed
from py_scripts.filter_maf import FilterMaf

def writeMafChunk(blockSizes, chromSizes, mafSizes, blockChunks, blockChunkSizes,
                  names, lastAlignmentBounds, targetIndex, sourceIndex, filePrefix):

    numTargets = len(names)
    numSources = len(names)
    currentMaf = old_div(sum(mafSizes), 2)
    lastMafChunk = len(blockChunkSizes) == len(blockChunks) and len(blockChunkSizes[-1]) == 0

    sources = [[] for i in range(numTargets)]
    sourceNames = [
