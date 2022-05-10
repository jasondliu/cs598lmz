import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[1;32m')).start() # Color
from Simulator import *
from Combinatorics import *
from Utils import *
import copy
from tqdm import tqdm
import matplotlib.pyplot as plt

class Tree():
    def __init__(self, node):
        self.node = node
        self.childs = []
        self.parent = None
        self.Q = 0
        self.cost = 0
        self.visited = False
        self.index = 0
        
    def add_child(self, node) :
        self.childs.append(node)
        node.parent = self
        
    def get_childs(self) :
        return self.childs
    
    def set_index(self, index):
        self.index = index
    
    def set_Q(self, Q):
        self.Q = Q
        
    def set_cost(self, cost):
        self.cost = cost
        
