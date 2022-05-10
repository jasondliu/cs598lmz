import ctypes
ctypes.cast(ctypes.py_object(x), ctypes.py_object).value

#%%
# https://stackoverflow.com/questions/5067604/determine-function-name-from-within-that-function-without-using-traceback
import inspect
inspect.currentframe().f_code.co_name

#%%
# https://stackoverflow.com/questions/15008758/parsing-boolean-values-with-argparse
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--foo', action='store_true')
parser.add_argument('--bar', action='store_false')
parser.add_argument('--baz', action='store_false')
args = parser.parse_args()

#%%
# https://stackoverflow.com/questions/12544056/how-do-i-find-the-first-and-last-index-of-some-value-in-a-list
l = [1, 2, 3, 4, 4, 5, 6, 4]

