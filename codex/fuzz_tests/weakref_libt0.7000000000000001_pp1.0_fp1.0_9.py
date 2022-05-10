import weakref
import logging
import platform
import rdflib
from rdflib import Literal
from rdflib import URIRef
from rdflib.namespace import RDF
from rdflib.namespace import RDFS
from rdflib.namespace import OWL


from .config import config
from .namespace import DCTERMS
from .namespace import FOAF
from .namespace import OV
from .namespace import RDF
from .namespace import RDFS
from .namespace import SKOS
from .namespace import SP
from .namespace import XSD

from .utils import hash_uri
from .utils import OrderedSet
from .utils import to_unicode

from . import __version__

from .xml_list import xml_list_to_list

from .cache_manager import cache_manager

from .resource import Resource
from .resource import ResourceFactory
from .resource import ResourceList

from .config import _

from . import core

from . import exceptions


def _get_graph(graph):

    if graph
