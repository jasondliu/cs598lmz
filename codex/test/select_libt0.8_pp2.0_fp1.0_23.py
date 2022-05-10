import select
from pymongo import MongoClient
import argparse
import sys
from time import time
from bson.objectid import ObjectId
from bson.code import Code
import json
from bson.son import SON
import py2neo.neo4j
import logging


logger = logging.getLogger(__name__)

def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-dd', '--doc_database', default='pubmed_central',
                        help='MongoDB database containing document fields')
    parser.add_argument('-co', '--collection', default='articles',
                        help='MongoDB collection containing document fields')
    parser.add_argument('-dc', '--document_fields', nargs='+',
                        help='Fields to be treated as document content')
