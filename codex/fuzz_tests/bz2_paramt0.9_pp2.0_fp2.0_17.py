from bz2 import BZ2Decompressor
BZ2Decompressor.flush = lambda self : bytes(0)

from dask.distributed import Client
from dask.bag import read_text

from dask_jobqueue import SLURMCluster

import matplotlib as mpl
mpl.use('Agg')
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from numpy import arange, pi
from io import BytesIO
import matplotlib.pyplot as plt

from tornado import gen
from tornado.web import RequestHandler, Application, url
from tornado.ioloop import IOLoop
from tornado.process import Subprocess

from urllib.parse import parse_qsl

from datetime import timedelta
from time import time

from netrc import netrc

_b = BytesIO()

def plot(x,y):
    fig = Figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot(x,y)
    FigureCanvas(fig).print_png(_b)
   
