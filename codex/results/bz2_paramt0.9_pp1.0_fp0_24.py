from bz2 import BZ2Decompressor
BZ2Decompressor

from pathlib import Path

from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.namespace import DC, DCTERMS, FOAF, OWL, RDFS, Namespace, SKOS, XSD
from rdflib.plugins.sparql import prepareQuery
from rdflib.plugins.sparql.results.jsonresults import JSONResultSerializer
from rdflib.plugins.sparql.results.xmlresults import XMLResultSerializer

import csv

from concurrent.futures import as_completed



from dotenv import load_dotenv
load_dotenv()

## Setup dbpedia credentials
apiKey = os.getenv("DBPEDIA_KEY")
if apiKey is not None:
    headers={
        "Authorization": "Basic "+b64encode(apiKey.encode('utf-8')).decode('utf-8')
    }
else:
    headers=None
    print("DBPEDIA_KEY not set. Running without authorization")
