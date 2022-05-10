import weakref

import numpy as np
import pandas as pd
import sklearn as sklearn
import xgboost as xgb

from autosklearn.pipeline.components.base import \
    AutoSklearnClassificationAlgorithm
from autosklearn.pipeline.constants import *
from autosklearn.pipeline.implementations.util import softmax
from autosklearn.util import get_metric


class XGBTree(AutoSklearnClassificationAlgorithm):
    def __init__(self,
                 loss='multi:softprob',
                 learning_rate=0.1,
                 n_estimators=100,
                 max_depth=3,
                 min_child_weight=1,
                 subsample=1.0,
                 colsample_bynode=1.0,
                 colsample_bylevel=1.0,
                 colsample_bytree=1.0,
                 reg_alpha=0.0,
                 reg_lambda=1.0,
                 gamma=0.0,
                 max_delta_step=0.
