import ctypes
ctypes.cdll.LoadLibrary('libX11.so')

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

from PIL import Image, ImageTk
import numpy as np
import tkinter as tk

from sklearn.cluster import KMeans, DBSCAN
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.metrics import silhouette_score, calinski_harabaz_score

from gensim.models.word2vec import Word2Vec

from scipy.stats import spearmanr

import codecs

import argparse

parser = argparse.ArgumentParser(description='Visualize word embeddings')
parser.add_argument('--w2v', type=str,
                    help='path to the word2vec model')
parser.add_argument('--w2v_format', type=str,
