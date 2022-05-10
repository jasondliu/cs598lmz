from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open('../data/categories_en.ttl.bz2').read())

from rdflib import Namespace, Graph
from rdflib.namespace import RDF
g = Graph()
g.parse('../data/categories_en.ttl', format='n3')

print(len(g))
g.serialize(destination='../data/categories_en.rdf', format='xml')

len(g)
ns = Namespace("http://dbpedia.org/resource/Category:")

cat = ns['Category']
for s, p, o in g.triples((None, RDF.NS, cat)):
    print(s, p, o)
    break

cat = ns['Category']
for s, p, o in g.triples((None, RDF.NS, cat)):
    print(s, p, o)
    break

for s, p, o in g.triples((None, RDF.NS, cat)):
    if str(s).endswith("Deep_learning
