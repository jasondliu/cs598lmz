import lzma
lzma.LZMA_AVAILABLE
print("lzma is available")
import lzma
outFile = open("file.out.lzma", "wb")
compressor = lzma.LZMACompressor()
outFile.write(compressor.compress(b"wibble"))
outFile.write(compressor.flush())
outFile.close()
from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.namespace import DC, FOAF

g = Graph()

# Create an identifier to use as the subject for Donna.
donna = BNode()

# Add triples using store's add method.
g.add( (donna, RDF.type, FOAF.Person) )
g.add( (donna, FOAF.nick, Literal("donna", lang="foo")) )
g.add( (donna, FOAF.name, Literal("Donna Fales")) )
g.add( (donna, FOAF.mbox, URIRef("mailto
