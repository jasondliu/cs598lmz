import codecs
codecs.register_error('strict', codecs.ignore_errors)

import pyximport; pyximport.install()

import os, sys, pprint, time, glob
import cPickle as pickle

import numpy as np
import numpy.random as npr

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from sklearn.mixture import GMM
from sklearn import linear_model

from blocks.algorithms import GradientDescent, Adam, RMSProp, Scale, AdaDelta, CompositeRule, StepClipping, Momentum
from blocks.extensions import Printing
from blocks.extensions.monitoring import DataStreamMonitoring
from blocks.extensions.plot import Plot
from blocks.filter import VariableFilter
from blocks.graph import ComputationGraph, apply_dropout
from blocks.initialization import IsotropicGaussian, Constant, Orthogonal
from blocks.main_loop import MainLoop
from blocks.model import Model
from blocks.roles import PARAMETER
from fuel.datasets import IterableDataset, DataStream

