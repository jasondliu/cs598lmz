import threading
threading.stack_size(2**27)
import sys
import copy
sys.setrecursionlimit(10**7)

def pv(val, message_option=False):
    if message_option:
        print(val)
    return

def pa(val, message_option=False):
    if message_option:
        print('\n'.join(map(str, val)))
    else:
        print(val)
    return

def ppa(val, message_option=False):
    if message_option:
        print('\n'.join(map(lambda x: '\n'.join(map(str, x)), val)))
    else:
        print(val)
    return

def matrix_to_list(matrix, data_type):
    list_matrix = []
    for i in range(len(matrix)):
        list_matrix.append([])
        for j in range(len(matrix[0])):
            list_matrix[-1].append(data_type(matrix[i][j]))
   
