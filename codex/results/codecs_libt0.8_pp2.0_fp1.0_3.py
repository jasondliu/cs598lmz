import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

import urllib.request
import re
import sys, os
import time

def get_html(url):
    send_headers = {
    }

    request = urllib.request.Request(url=url, headers=send_headers)
    res = urllib.request.urlopen(request)
    return res.read()

def get_html_content(url):
    html = get_html(url)
    return html.decode('utf8')

def download_file(url):
    url_obj = urllib.parse.urlparse(url)
    fname = url_obj.path.split('/')[-1]
    if os.path.exists(fname):
        print(fname, "exists")
        return url
    #os.makedirs(fname)
    #with open(fname, "wb") as f:
    #    req = requests.get(url)
    #
