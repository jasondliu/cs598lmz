import _struct
import json
import requests
import time
import urllib.parse

class RestClient:
    '''A simple REST client'''

    default_headers = {}
    default_proxies = {}
    default_retries_on_failure = 3

    def __init__(self,
                 base_url = '',
                 headers = None,
                 proxies = None,
                 retries_on_failure = None):
        '''
        Constructor

        :param base_url: The base URL for all API calls
        :param headers: An optional dictionary of headers to add to all API calls
        :param proxies: An optional dictionary of proxies to use for API requests
        :param retries_on_failure: How many times to retry after a failure
        '''
        self.base_url = base_url

        if headers is not None:
            self.default_headers = headers

        if proxies is not None:
            self.default_proxies = proxies

        if retries_on_failure is not None:
            self.default_retries_on_
