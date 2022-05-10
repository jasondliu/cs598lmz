import threading
threading.stack_size(67108864)
from operator import itemgetter
import networkx as nx
import matplotlib.pyplot as plt
import PIL
from PIL import Image
from wordcloud import WordCloud, STOPWORDS



def create_data_structure():
    data = {'nodes': [], 'edges': []}
    return data

def add_to_data_structure(data, name, id, email_address= None, work_place= None, school= None, company= None, college= None, events_participated= None, friends= None):
    '''
        This function is used to add a node to the data structure.
    '''
    for node in data['nodes']:
        if node['id'] == id:
            node['name'] = name
            return
