import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)


# Imports MySQL Confiuration from Config File
with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '/mysql.json') as json_config_file:
	 Config = json.load(json_config_file)


# App Engine Imports
from google.cloud import datastore
from google.cloud import storage
from google.cloud import translate
from google.cloud import speech
from google.cloud import language
from google.cloud import vision
from google.cloud.language import enums
from google.cloud.language import types
from google.cloud import texttospeech
from google.cloud import language_v1
from google.cloud.language_v1 import enums
from google.cloud import bigquery
from google.cloud.texttospeech import enums
from google.cloud.storage import Blob
from google.cloud import pubsub_v1



# Imports MySQL Database
