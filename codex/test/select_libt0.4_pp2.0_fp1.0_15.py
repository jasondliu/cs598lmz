import select_data
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
from matplotlib.dates import DateFormatter
import matplotlib.ticker as ticker

def main():
    #get data
    data = select_data.main()
    #print(data)
    #get dates
    dates = data[:,0]
    #print(dates)
    #get values
    values = data[:,1]
