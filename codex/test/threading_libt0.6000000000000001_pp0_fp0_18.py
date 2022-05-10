import threading
threading.stack_size(32768)

from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from django.conf import settings

from ...models import *
from ...utils import *
from ...utils.decorators import *

from ... import tasks

from bs4 import BeautifulSoup
from datetime import datetime
import requests
import json
import time
import random
import re

class Command(BaseCommand):

	help = '''
			Scraps all the users in the database, and then their followers and friends
			'''

	def __init__(self, *args, **kwargs):
		super(Command, self).__init__(*args, **kwargs)
		self.user_id = None
		self.user_name = None
		self.user = None

