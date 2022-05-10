import signal
signal.alarm(3600)
import sys, os


def read_input(kb):
   for i in itertools.repeat(None, kb):
      i = sys.stdin.readline().rstrip().replace('X','0')
      if not i:
          return
      yield i


import itertools, sys
from collections import defaultdict
import random
from gurobipy import *
from tsp_solver import Params, solve_tsp



def main():
  board = []
  all_num = []
  n = 1
  word_len = 0
  num_link =0
  num_word = 0
  set_index =0
  hor_set =set()
  vert_set = set()
  vert_dic = defaultdict(list)
  left_dic = defaultdict(list)
  right_dic = defaultdict(list)
  for i in read_input(4):
    board.append(i)
    all_num.extend(list(i.replace('X','0')))
    for j
