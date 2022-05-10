import mmap
import math
from random import randint
from py2neo import Graph, Node, Relationship
from Levenshtein import *
from tokenizer import *
#from textblob import *
#from textblob.classifiers import NaiveBayesClassifier
#from textblob import Blobber
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
#from sympy.physics.wigner import wigner_6j
import sys
class Concept:
    def __init__(self, concept, parent_id, ):
        self.concept = concept
        self.probability = None
        self.parent = []
        self.count = None
        self.parent_id = parent_id
        self.child = []
        self.child_sim = []
        self.child_concept_rdfs = []
        self.child_concept_rdf = None
        self.child_id = None
