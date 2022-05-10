import gc, weakref
import logging

import numpy as np
import pandas as pd

from . import utils
from . import config
from . import data
from . import model
from . import metrics
from . import plot
from . import exceptions

logger = logging.getLogger(__name__)

class Experiment(object):
    """
    An experiment is a collection of models and data.

    Parameters
    ----------
    name : str
        Name of the experiment.
    data : Data
        Data object.
    models : list of Model
        List of models to be trained.
    metrics : list of Metric
        List of metrics to be evaluated.
    """
    def __init__(self, name, data, models, metrics):
        self.name = name
        self.data = data
        self.models = models
        self.metrics = metrics
        self.results = {}
        self.plots = {}

    def run(self, n_epochs=None, n_epochs_per_model=None, n_epochs_per_metric=
