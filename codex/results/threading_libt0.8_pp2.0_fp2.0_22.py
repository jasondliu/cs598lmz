import threading
threading.stack_size(66000000)

from bs4 import BeautifulSoup
import requests

from multiprocessing import Process, Manager, current_process
from multiprocessing.pool import ThreadPool

from collections import defaultdict

import itertools
import pickle
import os

from datetime import datetime, timedelta
import time
import random

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from tqdm import tqdm
import multiprocessing

import json

import re
import csv


def save_obj(obj, name ):
    with open("data/" + name + ".pkl", 'wb') as f:
        pickle.dump(obj, f, pickle
