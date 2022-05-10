import codecs
codecs.register_error('strict', codecs.ignore_errors)
from slackclient import SlackClient
from itertools import chain
import string
from fuzzywuzzy import fuzz
import pyrebase
from random import randint
import requests
from firebase.firebase import FirebaseAuthentication, FirebaseApplication, FirebaseApplication
import json
from tf_idf_matrix import get_misspell
import numpy as np

import sys
reload(sys)
sys.setdefaultencoding('utf8')

config = {
  "apiKey": "AIzaSyBNNhlpKYnOMiHzUpKdvyxciMvOk8YMtjE",
  "authDomain": "menagerie-c5f48.firebaseapp.com",
  "databaseURL": "https://menagerie-c5f48.firebaseio.com/",
  "storageBucket": "menagerie-c5f48.appspot.com"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
user = auth.sign_
