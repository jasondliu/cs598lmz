import select_data
import datetime
import pytz

def get_fetch_time():
    fetch_time = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
    fetch_time = fetch_time.strftime('%Y-%m-%d %H:%M:%S')
    return fetch_time

def get_fetch_time_for_filename():
    fetch_time = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
    fetch_time = fetch_time.strftime('%Y-%m-%d_%H%M%S')
    return fetch_time

def get_fetch_time_for_filename_for_staging():
    fetch_time = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
    fetch_time = fetch_time.strftime('%Y-%m-%d_%H%M')
    return fetch_time

def get_fetch_time_for_filename_for_prod():

