from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# pympler
# $ python -m pympler.run <your-program.py>
# $ python3 -m pympler.run <your-program.py>

import pympler.asizeof
pympler.asizeof.asizeof(your_object)

# kcachegrind, graphviz
# $ pip install pycallgraph

from pycallgraph import PyCallGraph
from pycallgraph import Config
from pycallgraph import GlobbingFilter
from pycallgraph.output import GraphvizOutput
config = Config()
config.trace_filter = GlobbingFilter(exclude=[
    'pycallgraph.*',
    '*.secret_function',
])
graphviz = GraphvizOutput()
graphviz.output_type = 'svg'

with PyCallGraph(output=graphviz, config=config):
    # Your normal program code goes here
    a = YourObject()
    a.draw()

# lineprof (uses snakeviz)
# $ pip install snakeviz
# $ pip
