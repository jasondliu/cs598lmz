import threading
threading.Thread(target=lambda: webbrowser.open('http://localhost:9000/')).start()

#TODO: make graphviz generate a picture, not a pdf.
#TODO: fix error handling
#TODO: improve styling

import networkx
networkx.Graph().__init__()

#from graphviz import Digraph
#from graphviz import Graph

from networkx.drawing.nx_agraph import graphviz_layout
from IPython.display import SVG, display
from IPython.core.display import display, HTML
import json

#from graphviz import Source
#import cairosvg
#import io


#from IPython.display import HTML
#from IPython.display import SVG, display
#from IPython.display import Image
#from IPython.utils.safeeval import *
#from IPython.core.display import HTML
#from IPython.display import Image
#from IPython.display import display
#from IPython.display import SVG
#from IPython.display import Image
#from IPython.display import display
