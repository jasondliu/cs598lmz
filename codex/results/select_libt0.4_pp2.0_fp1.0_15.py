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
    #print(values)

    #convert dates to datetime object
    dates = [datetime.strptime(date, '%Y-%m-%d') for date in dates]
    #print(dates)

    #plot data
    plt.plot(dates,values)

    #format date axis
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(
