import mmap
import os
import sys
import zlib

from pprint import PrettyPrinter

def hash(x):
    return hashlib.sha256(str(x)).hexdigest()

def dist(x, y):
    #x = np.array(x)
    #y = np.array(y)
    x = np.array(x[0:3])
    y = np.array(y[0:3])
    return np.linalg.norm(x - y)

def dist_squared(x, y):
    return dist(x, y)**2

class Data(object):
    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.good_data = root_dir + "good/"
        self.bad_data = root_dir + "bad/"
        self.json_dir = root_dir + "json/"
        self.database = root_dir + "database.db"
        self.test_file = root_dir + "test.json"
        self.good = Good
