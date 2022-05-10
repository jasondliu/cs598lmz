import gc, weakref
from . import _aag2
from ._aag2 import PlotItem, SigItem
import numpy as np

__all__ = ['AAGplot']

class AAGplot:
    def __init__(self, data, aa, mapdesc, strate=50):
        self.data = data
        self.aa = aa
        self.mapdesc = mapdesc
        self.strate = strate
    
    def show(self):
        _aag2.launch(self)
    
    def setData(self, data):
        self.data = data

def run():
    import os, sys, time
    import PyQt5.QtGui as qg
    import PyQt5.QtWidgets as qw
    import PyQt5.QtCore as qc
    
    def fun1(z, t, a,b,c,d,e,f,g):
        return (z*t+2).astype(np.float32)
    
    def fun2(t, a,b,c,
