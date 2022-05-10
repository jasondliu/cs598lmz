import codecs
codecs.register_error('replace_with_space', lambda e: (u' ',e.start + 1))
import pandas as pd
import requests
import bs4
import dc_stat_think as dcst
import seaborn as sns
import toolz as tz
import pickle
import datetime
import matplotlib.pyplot as plt

%matplotlib inline
 
def get_html(url):
    response = requests.get(url)
    return bs4.BeautifulSoup(response.text, 'lxml')

def save_pkl(obj, filename):
    with open(filename, 'wb') as f:
        pickle.dump(obj, f, protocol=2)

def load_pkl(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

html_mlb = get_html('http://m.mlb.com/gdcross/components/game/mlb/year_2018/month_08/day_09/master_scoreboard.json')
decoded = json.
