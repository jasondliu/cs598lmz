import mmap
import os
import ctypes
import cProfile
import re

def get_size(df):
    src_size = df.size
    print('Size: ', src_size)
    print('{:<20} {:.2f} GB'.format('DataFrame size:',src_size * 8 / 1024 / 1024 / 1024))
    print('{:<20} {:.2f} Mb'.format('DataFrame size:',src_size * 8 / 1024 / 1024))
    print('{:<20} {:.2f} Kb'.format('DataFrame size:',src_size * 8 / 1024))
    print('{:<20} {:.2f} B'.format('DataFrame size:',src_size * 8))
    mm = src_size*8/1024/1024/1024
    gb = mm/1024
    return gb

def get_mem_usage(df, format='MB'):
    if format == 'MB':
        return df.memory_usage(deep=True).sum() / 1024**2
    else:
        return df.memory_usage
