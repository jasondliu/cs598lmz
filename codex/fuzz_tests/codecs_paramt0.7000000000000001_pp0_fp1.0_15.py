import codecs
codecs.register_error("strict", codecs.ignore_errors)

from rdflib.namespace import Namespace, RDF, RDFS, XSD
from rdflib import Graph, URIRef, Literal, BNode
from rdflib.plugins.sparql import prepareQuery

from rdf_utils import *

def get_all_facts(g):
	# get all facts
	facts = g.subjects(RDF.type, URIRef("http://ontology.dumontierlab.com/Fact"))
	
	# get all facts that are part of a more specific fact
	facts_part = g.subjects(RDF.type, URIRef("http://ontology.dumontierlab.com/FactPart"))
	
	# remove facts that are part of more specific facts
	facts = [f for f in facts if f not in facts_part]
	
	return facts

def get_all_observations(g):
	# get all observations
	return g.subjects(RDF.type, URIRef("http://ontology
