import threading
threading._DummyThread._Thread__stop = lambda x: 42

import logging

from openbayes import BNet, BVertex
from openbayes import BDeuScore
from openbayes.learners import ConstraintBasedLearner


class TestConstraintBasedLearner(unittest.TestCase):
    def setUp(self):
        self.net = BNet('Earthquake Control')
        self.e = BVertex(0, 'earthquake', ['t', 'f'], range(2))
        self.b = BVertex(1, 'burglary', ['t', 'f'], range(2))
        self.a = BVertex(2, 'alarm', ['t', 'f'], range(2))
        self.j = BVertex(3, 'johncalls', ['t', 'f'], range(2))
        self.m = BVertex(4, 'marycalls', ['t', 'f'], range(2))
