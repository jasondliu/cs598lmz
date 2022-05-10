import codecs
codecs.register_error('strict', codecs.ignore_errors)

import csv
import re
import urllib

class CSVWriter(object):
    def __init__(self, filename, headers, fieldnames):
        self.writer = csv.DictWriter(open(filename, 'w'),
                                     fieldnames=fieldnames)
        self.writer.writerow(dict(headers))

    def write(self, data):
        self.writer.writerow(data)
        

def parse():
    url = 'http://www.gadm.org/download_country_v2.html'
    headers = [('country_name', 'Country'),
               ('region_name', 'Region'),
               ('region_code', 'ISO/FIPS'),
               ('shape_file', 'Shape file'),
               ('arc_file', 'ARC file')]
    fieldnames = [h[0] for h in headers]
    writer = CSVWriter('data/gadm-countries.csv', headers, fieldnames)

    r = urllib.urlopen(url)
    html = r
