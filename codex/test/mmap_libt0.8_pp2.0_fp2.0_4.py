import mmap
import numpy as np
from functools import reduce
import operator
import os
from msmbuilder.msm import MarkovStateModel
from msmbuilder.msm.estimators.maximum_likelihood_msm import MaximumLikelihoodMSM
from msmbuilder.msm.estimators.bayesian_markov_chain_monte_carlo import BayesianMarkovChainMonteCarlo
from msmbuilder.msm.estimators.bayesian_markov_chain_monte_carlo import BayesianMSM as MSM



