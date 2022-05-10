import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Avoid futurewarnings
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=UserWarning)

# Connect to the database
engine = create_engine('mysql+mysqlconnector://root:@localhost:3306/twitter_db', echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
db_session = Session()

# Scraping imports
from selenium.webdriver.chrome.options import Options as CH_Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Helper functions
import re
import urllib.parse
import urllib.request

