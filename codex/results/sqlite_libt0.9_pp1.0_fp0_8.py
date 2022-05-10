import ctypes
import ctypes.util
import threading
import sqlite3
import json
import time

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

class Adress():
    def __init__(self):
        self.nodes=[]
        self.arr=[0,0,0] #x,y,z
    def updata(self):
        self.arr[0]=self.nodes[0].arr[0]
        self.arr[1]=self.nodes[1].arr[1]
        self.arr[2]=self.nodes[2].arr[2]


class Node():
    def __init__(self):
        self.arr=[0,0,0]

class Tiling():
    def __init__(self):
        self.size=50
        self.nodes=[]
        for i in range(self.size):
            self.nodes.append([])
            for j in range(self.size):
                self.nodes[i].append(Node())
    def get
