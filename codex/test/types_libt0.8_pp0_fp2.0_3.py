import types
types.ClassType=type

#sys.path.insert(0, '../../c/src/wrapper')
import clib

def get_input():
    return open('input.pdb').read()

def main():
    ret = clib.compute_centroids(get_input())
