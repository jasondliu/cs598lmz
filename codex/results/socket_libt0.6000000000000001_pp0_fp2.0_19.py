import socket
import time
import datetime
import random
import json
import requests
import sys

# --------------------------------------------------
# Global variables
# --------------------------------------------------

# --------------------------------------------------
# Global functions
# --------------------------------------------------

# --------------------------------------------------
# Class definitions
# --------------------------------------------------

# --------------------------------------------------
# Main program
# --------------------------------------------------

def main():
    # Read the list of sensors from the file
    filename = "sensors.txt"
    sensors = []
    with open(filename, 'r') as f:
        for line in f:
            tokens = line.split()
            sensors.append(tokens[0])

    # Create the dictionary of data
    data = {}
    for sensor in sensors:
        data[sensor] = {'value': 0, 'timestamp': 0}

    # Keep sending data for each sensor
    for sensor in sensors:
        # Create the sensor name
        sensor_name = "sensor_" + sensor

        # Create the URL for the POST request
        url = "http://127.0.0.1:5000/api
