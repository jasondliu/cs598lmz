import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)

import requests
import gzip
import json
import re
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-a', '--author', required=True,
        help='Name of author'
    )
    parser.add_argument('-t', '--tweets', default=999,
                        help='Numbers of tweets to scrape.')

    parser.add_argument(
        '-l', '--lang', required=False,
        help='Author language. E.g. en'
    )

    parser.add_argument(
        '-f', '--file', required=False,
        help='Output json file name.'
    )

    return parser.parse_args()

class TwScrape(object):

    def __init__(self, targetUser):

        self.targetUser = targetUser
        self.target_api = 'https://twitter.com/
