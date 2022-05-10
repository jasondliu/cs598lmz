import mmap
import numpy as np
import time
import os
import sys

"""
This file is part of the computer assignments for the course DD1418/DD2418 Language engineering at KTH.
Created 2017 by Johan Boye, Patrik Jonell and Dmytro Kalpakchi.
"""

class KneserNeySmoothing:
    """
    This class implements Kneser-Ney smoothing.
    """

    def __init__(self, ngram_counts, delta=1.0, D = 0.75):
        """
        This is the class constructor.
        """
        self.delta = delta # The delta parameter.
        self.D = D # discounting factor
        self.ngram_counts = ngram_counts # An ngram counter object.
        self.ngram_probs = {} # Dictionary for storing ngram probabilities.
        self.discounts = {} # Dictionary for storing discounts.

    def train(self):
        """
        This function implements the training of the Kneser-Ney smoothing model.
        """
        #
