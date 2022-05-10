import threading
threading.stack_size(2**27)
import sys
import math
from lxml import etree
import re
import tldextract
sys.setrecursionlimit(10**7)
#El programa esta basado en las diapositivas de la asignatura
def load_stopwords(STOP_WORDS_FILE):
  with open(STOP_WORDS_FILE, "r",encoding="utf-8") as f:
    return set([w.strip().replace(' ', '_') for w in f.readlines()])

def Jaccard (A, B):
    set_A = set(A)
    set_B = set(B)
    jaccard_val = len(set_A.intersection(set_B))/len(set_A.union(set_B))
    return jaccard_val

def Jaccardposition(A, B):
    set_A = set(A)
    set_B = set(B)
    jaccard_val = (len(set_A.intersection(set_B
