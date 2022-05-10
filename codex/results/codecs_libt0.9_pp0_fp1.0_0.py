import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)
import numpy as np
import numpy.matlib
import pandas as pd
from scipy.interpolate import interp1d


def windData(filename, Uref):
    # Read energyPlus wind file into dataframe
    df = pd.read_csv(filename, sep=',', comment='#', usecols=[0, 4, 1])
    df = df.drop_duplicates()
    df = df.rename(columns={'Date/Time': 'Date',
                            'Hdd (KJ/m2)': 'Hour',
                            'Wind Dir': 'WindDir',
                            'Wind Speed (mps)': 'WindU'})

    # Add time column and convert time to number of seconds
    df['timestamp'] = df['Date'] + ' ' + df['Hour']
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.Date = df.timestamp
