import io
# Test io.RawIOBase so that stdin is captured
# from: http://stackoverflow.com/questions/7654375/unit-testing-python-input
def get_input(user_input):
  stdin = sys.stdin
  sys.stdin = io.StringIO(user_input)
  yield
  sys.stdin = stdin
import pandas as pd
import numpy as np
import scipy as sp
