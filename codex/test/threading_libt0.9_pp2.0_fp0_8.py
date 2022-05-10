import threading
threading.stack_size(10**8)  # new thread will get stack of such size
start = time.time()

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from sklearn.externals import joblib 

df = pd.read_csv("test.csv")


def pre_process():
    global df
    df = df.drop(['id'], axis=1)
    cols_encoder = [i for i in df.columns if df[i].dtype==object]
    df[cols_encoder]=df[cols_encoder].apply(LabelEncoder().fit_transform)
    scaler = StandardScaler()
    df_final = pd.DataFrame(scaler.fit_transform(df))
    
def predict():
    global df
    n=joblib.load('n_value.pkl')
    theta_vector=joblib.load('theta_vector.pkl')

