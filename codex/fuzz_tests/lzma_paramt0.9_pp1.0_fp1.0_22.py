from lzma import LZMADecompressor
LZMADecompressor().decompress(import_graph_def)
Image(raw_data=import_graph_def)
from IPython.display import HTML
HTML('<html><head><link rel="stylesheet" href="src/main/resources/custom.css" type="text/css"/></head><body style="background-color: #00000000">' + import_graph_def + '</body></html>')
from tensorflow.core.framework.graph_pb2 import GraphDef
from tensorflow.core.framework.versions_pb2 import VersionDef
from google.protobuf import text_format
from IPython.display import HTML

tensorboard_graph = GraphDef()
with open(grf_path, 'r') as f:
    text_format.Merge(f.read(), tensorboard_graph)

import_graph_def = text_format.MessageToString(tensorboard_graph)

HTML('<html><head><link rel="stylesheet" href="src/main/resources/custom.css" type="text/css"/></head><body style="background-color
