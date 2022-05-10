import ctypes
import ctypes.util
import threading
import sqlite3
import json
import gc

# define a global variable

TEST = None

class Test():
    """
    Test class
    """
    def __init__(self, name):
        self.name = name



def get_test():
    """
    get test class
    :return:
    """
    return TEST

def set_test(test):
    """
    set test class
    :param test:
    :return:
    """
    global TEST
    TEST = test

def add_test():
    """
    add test class
    :return:
    """
    global TEST
    TEST.name += "1"


def test_lib_path():
    """
    test lib path
    :return:
    """
    print("test lib path:")
    print(ctypes.util.find_library("c"))




def test_ctypes():
    """
    test ctypes
    :return:
    """
    libc = ctypes.cdll.LoadLibrary(ctypes.util.find_library("c
