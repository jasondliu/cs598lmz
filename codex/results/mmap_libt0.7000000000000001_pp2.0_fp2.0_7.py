import mmap
import matplotlib.pyplot as plt
import numpy as np
import json
from scipy.signal import savgol_filter
import matplotlib.dates as mdates
from datetime import datetime, timedelta


def main():
    # load the data
    data = json.load(open('../../data/sensor_data/sensor_data.json'))

    # get the time from the data
    time = data['time']
    time = np.array(time)
    time = time - time[0]  # start at zero
    time2 = time/1000  # convert to seconds

    # get the temperature data
    temperature = data['temperature']
    temperature = np.array(temperature)

    # get the pressure data
    pressure = data['pressure']
    pressure = np.array(pressure)

    # get the humidity data
    humidity = data['humidity']
    humidity = np.array(humidity)

    # plot the data
    fig, ax = plt.subplots(3)

    # plot temperature and humidity

