import sys, threading
threading.Thread(target=lambda: sys.stdout.write('')).start()

sys.path.append('../')
import numpy as np
from math import log
import wavelet.waveletFunctions as waveFuncs
import wavelet.plotWavelet as plotWavelet
import Utils.graphTools as graphTools
import pywt
import networkx as nx

def waveletGraph(data, wavelet, postfiltering=True, a=2):
    w = waveFuncs.constructWavelet(wavelet, data, a)
    weights = np.abs(w)

    graph_weights = np.ones((len(data),len(data))) # weights of the wavelet graph
    for i in range(1,len(data)-2):
        for j in range(i+1,len(data)):
            if (postfiltering and ((w[i]*w[j])<0)) or (not postfiltering):
                graph_weights[i][j] = weights[i]*weights[j]

    #G = nx.from_numpy_matrix(graph_weights)
   
