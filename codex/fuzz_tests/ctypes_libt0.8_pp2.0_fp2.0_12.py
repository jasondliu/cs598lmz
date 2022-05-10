import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('a')
from mail import mail
from data import data_process
from chart import chart
from pymongo import MongoClient
import datetime
import pandas as pd

class freq():
    def __init__(self, start_time, end_time, freq):
        self.parsed_start_time = self.parse(start_time)
        self.parsed_end_time = self.parse(end_time)
        self.freq = freq
        self.client = MongoClient()
        self.db = self.client['stock']
        self.collection_raw = self.db['raw']
        self.collection_last = self.db['last']

    def parse(self, date_string):
        return datetime.datetime.strptime(date_string, '%Y-%m-%d')

    def get_data(self):
        # Load data from mongodb
        self.raw_data = pd.DataFrame(list(self.collection_
