import select

from bs4 import BeautifulSoup
from jinja2 import Environment, PackageLoader, select_autoescape
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.proxy import Proxy, ProxyType

from urllib.request import urlopen
from urllib.parse import urlparse
from urllib.parse import urljoin
from urllib.error import HTTPError
from urllib.error import URLError

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType

from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from selenium
