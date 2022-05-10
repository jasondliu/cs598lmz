import codecs
codecs.register(take_all)
import click
import sparql
import types
import json


def get_data(uri):
    endpoint = sparql.Service("http://live.dbpedia.org/sparql", "utf-8", "GET")
    endpoint.setMethod("GET")
    query = sparql.Query("""
    PREFIX dbo:<http://dbpedia.org/ontology/>
    PREFIX dbr:<http://dbpedia.org/resource/>
    PREFIX dbp:<http://dbpedia.org/property/>
    PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
    PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX foaf:<http://xmlns.com/foaf/0.1/>
    PREFIX yago:<http://dbpedia.org/class/yago/>
    PREFIX owl: <http://www.w3.org/2002/07/owl#
