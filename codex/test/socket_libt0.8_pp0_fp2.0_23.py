import socket

from scraper import Scraper

class Parser(object):
    """Pulls JSON data from the API and parses it into a PHP script"""

    def __init__(self, url, endpoint=None, subdir=None, verbose=False):
        """Create a new Parser.

        :param string url: The URL of the API to parse data from
        :param string endpoint: The endpoint to query at the API
        :param string subdir: The subdirectory to save results in
        :param bool verbose: Should this parser output extra information?
        """
        self.url = url
        # TODO: Make this a default if nothing is specified
        self.endpoint = endpoint or 'api/v0.1/'
        # TODO: Make this a default if nothing is specified
        self.subdir = subdir or './temp/'
        self.verbose = verbose

        # The API URL we'll be parsing from
        self.full_url = urlparse.urljoin(url, endpoint)

