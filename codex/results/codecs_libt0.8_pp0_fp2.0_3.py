import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

import csv
from scipy import stats
import glob
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set_context("poster")
sns.set_style("darkgrid")
sns.set_color_codes("colorblind")


# Read in the data

df = pd.read_csv("../data/at24_total.csv")
df_nas = df[(df['location'] == 'NAS')]
df_rma = df[(df['location'] == 'RMA')]
df_col = df[(df['location'] == 'COL')]
df_pao = df[(df['location'] == 'PAO')]

print(df_nas)
print(df_rma)
print(df_col)
print(df_pao)


# Plot the data

plt.scatter(
