import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('test_db.db')

from time import clock, time
from os import getpid
from os.path import isfile
from sys import exit
from argparse import ArgumentParser

from random import randint

from math import sqrt
from math import exp

from numpy.random import randn
from numpy import sum as npsum
from numpy import power as nppow
from numpy import array as nparray
from numpy import concatenate as npconcatenate
from numpy import arange as nparange
from numpy import take as nptake
from numpy import column_stack as npcolumn_stack
from numpy import empty as npempty
from numpy import int16 as npint16
from numpy import float32 as npfloat32
from numpy import float64 as npfloat64
from numpy import all as npall
from numpy import any as npany
from numpy import linalg as nplinalg
from numpy import loadtxt as nploadtxt
from numpy import ndarray as npnparray
from numpy import sort as npsort
