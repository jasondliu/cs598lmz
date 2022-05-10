import socket
import sys
import time
import threading
import random
import os
import math
import json
import pickle
import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import norm
from scipy.stats import multivariate_normal
from scipy.stats import multinomial
from scipy.stats import dirichlet

from sklearn.metrics import accuracy_score

from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import ComplementNB

from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import RidgeClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.linear_model import Perceptron

from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import RadiusNeighborsClassifier

from
