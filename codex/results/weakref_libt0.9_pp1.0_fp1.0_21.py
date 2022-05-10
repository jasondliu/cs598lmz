import weakref
import logging
import json
from argparse import ArgumentParser
from pathlib import Path
from ipywidgets import interact
import numpy as np

from cadet import Cadet
from cadet.graphics import OsmNodeGraphicsItem

from cadet_widget import CadetWidget
from source_node_widget import SourceNodeWidget
from sink_node_widget import SinkNodeWidget
from tqdm.notebook import tqdm
from plotly import graph_objects as go
from dash_mapbox import DashMapbox

logging.basicConfig(level=logging.INFO)
DashMapbox(access_token="pk.eyJ1Ijoic3Ryb25nYXplbnNjaGVkdWxlciIsImEiOiJjazNueG1haTQwMDE2M2hwbHNybzBkdGpvIn0.wFIVH_TWvrJc9RzvbsoW5A")


class ExampleCadetWidget(CadetWidget):
    def __init__(self, api_key,
