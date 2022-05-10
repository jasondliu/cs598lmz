import codecs
codecs.register_error('strict', codecs.ignore_errors)

import re

from operator import itemgetter

import os.path

import logging
logging.basicConfig(level=logging.INFO)

from itertools import izip

from collections import defaultdict

from yajl import yajl

#import pymongo

from elasticsearch import Elasticsearch


class ElasticsearchWriter:
    def __init__(self, es_host, es_index):
        self.es = Elasticsearch(hosts=[es_host])
        self.es_index = es_index

    def write(self, line):
        doc = yajl.loads(line)
        self.es.index(index=self.es_index, doc_type=str(doc['_type']), body=doc)


def get_files(dirs):
    for dir in dirs:
        for file in os.listdir(dir):
            if file.endswith('.json'):
                yield os.path.join(dir, file)

def process_files(
