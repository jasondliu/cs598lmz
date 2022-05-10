import select
import csv
import os
import time
import matplotlib.pyplot as plt
import numpy as np

class pca:
    def __init__(self,data,k):
        self.data=data
        self.k=k
        self.mean=np.mean(data,axis=0)
        self.data=data-self.mean
        self.cov=np.cov(self.data,rowvar=False)
        self.eigval,self.eigvec=np.linalg.eig(self.cov)
        self.reduced_data=self.data.dot(self.eigvec[:,:self.k])

def main():
    with open('wine.csv', 'rb') as f:
        reader = csv.reader(f)
        wine = list(reader)
    wine = np.array(wine[1:], dtype=np.float)
    pca_obj=pca(wine,2)
    print(pca_obj.reduced_data)
    plt.
