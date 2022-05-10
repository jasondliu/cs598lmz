import socket
socket.if_indextoname(2)

#%%

#%%

import numpy as np
np.arange(1,100, dtype=np.float16)

#%%

data = np.loadtxt('temperature.dat')
data

#%%

import matplotlib.pyplot as plt
plt.imshow(data)
plt.colorbar()

#%%

data = np.loadtxt('p001_data.csv', delimiter=',', skiprows=1)
plt.imshow(data)
plt.colorbar()

#%%

data = np.loadtxt('p001_data.csv', delimiter=',', skiprows=1)
plt.imshow(data)
plt.colorbar()
plt.savefig('MyImage.png', dpi=400, facecolor=(0,0,0))

#%%

import urllib.request

#%%

with open('p001_data.csv', 'wb') as f:
    url = 'https://covidtracking.com/api/
