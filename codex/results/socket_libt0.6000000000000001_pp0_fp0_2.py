import socket
from urllib.parse import urlparse

from bs4 import BeautifulSoup
import requests
from requests.exceptions import ConnectionError
from requests.exceptions import MissingSchema

from . import exceptions
from . import logger
from .schemes import SCHEMES_URLLIB_ALLOWED
from .utils import get_random_ua


class Fetch:
    """
    Fetch is a class that given a URL, will fetch the page and return the
    content of the page.
    """

    def __init__(self, url, timeout=15, proxy=None, verify=True, ua=None):
        """
        Initialize the Fetch object.
        :param url: The URL to crawl.
        :param timeout: The timeout for the request.
        :param proxy: The proxy to use for the request.
        :param verify: Verify SSL.
        :param ua: The user agent to use for the request.
        """
        self.url = url
        self.timeout = timeout
        self.proxy = proxy
        self.verify = verify
       
