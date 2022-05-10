import ctypes
ctypes.cdll.LoadLibrary('libopenblas.so')
ctypes.cdll.LoadLibrary('libatlas.so')
import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt

V = sio.loadmat('V.mat', squeeze_me=True)
V = V['V']
X = sio.loadmat('X.mat', squeeze_me=True)
X = X['X']

n, p = X.shape

def PCA(X, V, k=0):
    X = X.T
    if k == 0:
        k = p
    l = len(V)
    if k > l:
        k = l
    if k > 0:
        Vk = V[0:k, :]
    else:
        Vk = V
    Z = np.dot(X, Vk)
    return Z,Vk

def inverse(Z, Vk):
    Xk = np.dot(Z, Vk.T)
    return Xk

def
