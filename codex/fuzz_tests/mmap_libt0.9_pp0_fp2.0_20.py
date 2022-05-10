import mmap
import numpy as np
import time
import datetime
from numba import autojit, jit

from os import listdir
from os.path import isfile, join

from matplotlib import pyplot as plt
import seaborn as sns

from sklearn.cluster import KMeans

import matplotlib
matplotlib.rcParams['ps.fonttype'] = 42
matplotlib.rcParams['pdf.fonttype'] = 42

sns.set_style("white")
sns.set_palette("Blues", 5)
sns.set_context("poster")

def parseGTF(gtf_file,type="exon",feature=None):
    """
    gtf_file = GTF file with genome annotation
    """
    #gtf_file = "/media/laurent/My Book/Data_DNA/Annotation/gencode.v19.annotation.gtf"
    gtf_file_parsed = []
    colnames = ["gene_id","transcript_id","chrom","start","
