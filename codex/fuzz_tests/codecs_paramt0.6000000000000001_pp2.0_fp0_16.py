import codecs
codecs.register_error('strict', codecs.ignore_errors)

import os, sys, re, errno, time, random, copy, glob, datetime
from itertools import chain
from collections import defaultdict, OrderedDict
import gzip, cPickle, csv, json, lmdb, math, pprint

import numpy as np
import scipy.stats
import sqlite3

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import dates

import pandas as pd
from pandas import DataFrame, Series

import seaborn as sns
sns.set_style('white')
sns.set_context('notebook')

from IPython.display import display, HTML

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import pairwise_distances_argmin
from sklearn.metrics import silhouette_samples, silhouette_score

import tensorflow as tf

from keras.models
