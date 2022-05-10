import gc, weakref
#import matplotlib.pyplot as plt
from collections import defaultdict
from collections import Counter
import plotly.graph_objs as go
import plotly.plotly as py
import plotly
plotly.tools.set_credentials_file(username='ana_macedo', api_key='ZjnMeDwN1FtQ2QdJhLmv')


def load_database(name, limit=None):
    """Load a cPickle file and return the object it contains.
    """
    with open(name, 'rb') as f:
        loaded = cPickle.load(f)
    return loaded


def get_authors_in_cluster(cluster_id, author_cluster_dict):
    """Returns a list of authors in a cluster
    """
    return [k for k, v in author_cluster_dict.items() if v == cluster_id]

def get_authors(graph_object):
    """Returns a list with all the authors in the graph.
    """
    return [node[0] for
