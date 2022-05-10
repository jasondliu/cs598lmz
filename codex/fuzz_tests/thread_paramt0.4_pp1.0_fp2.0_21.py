import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import math
import random
import time

class Environment:
    def __init__(self, size):
        self.size = size
        self.grid = np.zeros((self.size,self.size))
        self.agent_pos = [0,0]
        self.goal_pos = [self.size - 1, self.size - 1]
        self.grid[self.agent_pos[0],self.agent_pos[1]] = 1
        self.grid[self.goal_pos[0],self.goal_pos[1]] = 2
        self.actions = ['up','down','left','right']
        self.action_dict = {'up':[-1,0],'down':[1,0],'left':[0,-1],'right':[0,1]}
    
    def reset(self):
        self.grid = np.zeros((self.size,self.size))
        self.agent_
