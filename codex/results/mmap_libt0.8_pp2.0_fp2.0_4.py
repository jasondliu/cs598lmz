import mmap
import numpy as np
from functools import reduce
import operator
import os
from msmbuilder.msm import MarkovStateModel
from msmbuilder.msm.estimators.maximum_likelihood_msm import MaximumLikelihoodMSM
from msmbuilder.msm.estimators.bayesian_markov_chain_monte_carlo import BayesianMarkovChainMonteCarlo
from msmbuilder.msm.estimators.bayesian_markov_chain_monte_carlo import BayesianMSM as MSM



def load_feature(filename):
    print 'Loading feature...'
    with open(filename, 'r') as f:
        buf = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        m = re.search(r'[\d.]+\n', buf)
        num_frames = int(m.group(0).strip())
        buf.seek(m.end(0))
        m = re.search(r'[\d.]+\n',
