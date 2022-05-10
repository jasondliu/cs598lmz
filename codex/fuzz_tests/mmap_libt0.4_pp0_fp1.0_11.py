import mmap
import os
import re
import sys
import time
import urllib2
import zipfile

from BeautifulSoup import BeautifulSoup

def get_urls(url):
    html = urllib2.urlopen(url)
    soup = BeautifulSoup(html)
    urls = [a['href'] for a in soup.findAll('a', href=re.compile(r'\.zip$'))]
    return urls

def download(url):
    print 'Downloading %s...' % url
    req = urllib2.Request(url)
    req.add_header('Referer', 'http://www.census.gov/geo/www/gazetteer/')
    zipdata = urllib2.urlopen(req).read()
    return zipdata

def unzip(zipdata, filename):
    print 'Unzipping %s...' % filename
    zipfile.ZipFile(StringIO.StringIO(zipdata)).extract(filename)
    return filename

def get_columns(filename):
    f
