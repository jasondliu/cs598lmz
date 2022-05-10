import ctypes
ctypes.cast(obj, ctypes.py_object).value

#list comprehension
[(i,j) for i in range(5) for j in range(5)]

#powerset
import itertools
#This is the way I need to use itertools
[set(i) for i in itertools.permutations([1,2,3])]

#other useful links:
#http://www.saltycrane.com/blog/2007/09/python-find-in-list/
#https://docs.python.org/2/library/itertools.html#recipes
#http://book.pythontips.com/en/latest/enumerate.html
#http://pymotw.com/2/sys/index.html
#https://stackoverflow.com/questions/17608287/how-to-change-a-list-into-a-string-python-3
#https://www.geeksforgeeks.org/python-loop-through-list-until-empty/
#https://stackoverflow.com/questions/142279
