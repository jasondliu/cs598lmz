from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed_data)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# Ensure CSV encoding is handled correctly
import os
from os import path as osp
import csv
import unicodedata
from rdflib import Graph, Namespace
from rdflib.namespace import RDF, RDFS, OWL
from rdflib.util import guess_format
from SPARQLWrapper import SPARQLWrapper, SQLWrapper
from benben.split_entity_types import get_namespaces, get_entity_types
from benben.env import load_env

env = load_env()
db_path = env['db_path']
parser_path = env['parser_path']
namespace_path = env['namespace_path']
download_path = env['download_path']

# =============================================================================
# Set up namespaces
# =============================================================================
namespaces = get_namespaces(namespace_path)
for ns_name, ns_uri in namespaces.items():
    globals()[ns_name.upper()] = Namespace(
