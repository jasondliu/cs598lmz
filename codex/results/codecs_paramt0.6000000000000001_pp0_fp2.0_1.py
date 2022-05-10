import codecs
codecs.register_error("strict", codecs.ignore_errors)
import pylab
import matplotlib.dates as mdates
import datetime
import locale
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
import matplotlib.animation as animation
from matplotlib import style
import csv
import re
import time
import datetime
import numpy as np

# create dictionary to hold the data

def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)

    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)

    return bytesconverter


def graph_data():
    style.use('ggplot')

    fig = plt.figure()

    ax1 = plt.subplot2grid((1, 1), (0, 0))

    stock_data = pd.read
