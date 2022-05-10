import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("/home/pi/pi-weather-station/pi-weather-station.db")

# Define a class to hold the data
class WeatherData:
    def __init__(self):
        self.temperature = 0.0
        self.pressure = 0.0
        self.humidity = 0.0

# Define a class to hold the calibration data
class CalibrationData:
    def __init__(self):
        self.t_fine = 0
        self.dig_T1 = 0
        self.dig_T2 = 0
        self.dig_T3 = 0
        self.dig_P1 = 0
        self.dig_P2 = 0
        self.dig_P3 = 0
        self.dig_P4 = 0
        self.dig_P5 = 0
        self.dig_P6 = 0
        self.dig_P7 = 0
        self.dig_P8 = 0
        self.dig_P9 = 0
        self.dig_H1 = 0
        self.dig_H2 = 0
        self.
