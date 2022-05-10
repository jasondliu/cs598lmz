import mmap
import numpy as np
from scipy.sparse import csr_matrix

# to add this directory to the path
import sys
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from src.algs.wb_cluster_tree import wb_cluster_tree


def main():
    # read the data
    filename = "../data/jain.txt"
    with open(filename, "r") as f:
        data = f.read()
    data = data.split("\n")
    n_points = len(data)
    n_features = int(data[0])
    data = [d.split(" ") for d in data[1:]]
