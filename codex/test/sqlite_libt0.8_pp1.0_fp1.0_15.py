import ctypes
import ctypes.util
import threading
import sqlite3 
import os
import pygame


def create_dir_if_not_exists(dirpath):
    if not os.path.isdir(dirpath):
        try:
            os.mkdir(dirpath)
        except OSError:
            print("Creation of the directory %s failed" % dirpath)
        else:
            print("Successfully created the directory %s " % dirpath)

def create_file_if_not_exists(filepath):
    if not os.path.isfile(filepath):
        try:
            open(filepath, 'x')
        except OSError:
            print("Creation of the file %s failed" % filepath)
        else:
            print("Successfully created the file %s " % filepath)
