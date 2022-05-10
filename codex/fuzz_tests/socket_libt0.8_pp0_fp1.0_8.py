import socket, json, bz2, glob, re, os, sys
import numpy as np
import pandas as pd
import xarray as xr

socket.setdefaulttimeout(3600)

first_date = pd.Timestamp('1900-01-01')
last_date = pd.Timestamp('2100-12-31')

def _get_dataset_names(dataset_str):
    if dataset_str is None:
        dataset_str = '*'
    directory = 'http://iridl.ldeo.columbia.edu/SOURCES/.Models/.NMME/.'
    datasets = glob.glob(directory + dataset_str)
    return datasets

def _parse_dataset_name(dataset):
    """
    Get the dataset name and description from the dataset's homepage.
    """
    try:
        ds_stream = urllib.request.urlopen(dataset)
        ds_page = ds_stream.read().decode('utf-8')
        ds_stream
