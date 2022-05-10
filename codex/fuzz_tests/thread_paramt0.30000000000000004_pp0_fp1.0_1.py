import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import pymc3 as pm
import theano.tensor as tt
from theano.compile.ops import as_op
from theano import shared
from theano.compile.ops import as_op
from theano import shared

#import pymc3.distributions.transforms as tr
from pymc3.distributions.transforms import t_stick_breaking
from pymc3.distributions.transforms import ElemwiseTransform
from pymc3.distributions.transforms import Transform
from pymc3.distributions.dist_math import bound, logpow, gammaln, betaln, binomln, betainc, logsumexp, logit, i0e, xlogy, i0, i1, expit, log1pexp, log1mexp, log1pexp,
