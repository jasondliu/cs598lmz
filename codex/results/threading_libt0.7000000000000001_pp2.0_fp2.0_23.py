import threading
threading.stack_size(67108864)

import requests
from bs4 import BeautifulSoup
from unidecode import unidecode
from datetime import datetime, timedelta
from django.db import connection
import time
from random import random

from core.models import Producto, Tienda, ProductoTienda

from django.utils import timezone
from django.db import connection
from django.db import transaction

from django.utils.dateparse import parse_datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options


from core.models import Producto, Tienda, ProductoTienda, ProductoTiendaHistorico
from django.utils.dateparse import parse_datetime
