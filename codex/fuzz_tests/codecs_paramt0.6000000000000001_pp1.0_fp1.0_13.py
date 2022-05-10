import codecs
codecs.register_error('strict', codecs.ignore_errors)

from datetime import datetime, timedelta

from flask import Flask, escape, request
app = Flask(__name__)

import requests

from google.cloud import storage
from google.cloud import bigquery
from google.oauth2 import service_account

import pandas as pd
import numpy as np

from bs4 import BeautifulSoup

storage_client = storage.Client()
bq_client = bigquery.Client()

dataset_id = 'covid_19'
table_id = 'covid_19_raw'
table_ref = bq_client.dataset(dataset_id).table(table_id)
table = bq_client.get_table(table_ref)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/covid_19_data')
def covid_19_data():
    try:
        # Grab the data
        r = requests.get('https://www.
