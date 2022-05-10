import select 
import time
import requests 
import urllib
import urllib2 
import json
import os


class GoogleVoice:
    """
    This class will allow you to send free SMS messages by scraping Google Voice
    It should be used for informational and research purposes only.

    """
    
    
    def __init__(self, email, passwd): 
        """
        Args: 
            email: Your Google email address
            password: Your Google password
        """
        
        self.email = email
        self.passwd = passwd
        self.token = self._getToken()
        self.r = requests.session()
        
    
    def _getToken(self): 
        """
        Retrieve the _rnr_se value used to send SMS messages
        """
        
        url = 'https://accounts.google.com/ServiceLogin?service=grandcentral&continue=https://www.google.com/voice#identifier'
