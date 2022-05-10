import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

import os
os.environ['PATH'] += ";C:\\Program Files (x86)\\Graphviz2.38\\bin"

import pygraphviz as pgv
import numpy as np

def GetGraph(op):
    graph = pgv.AGraph(directed=True)
    graph.graph_attr['rankdir'] = 'LR'
    graph.graph_attr['dpi'] = '200'

    # Find all inputs
    inputs = []
    for op_input in op.input:
        inputs.append(op_input.name)

    # Find all outputs
    outputs = []
    for op_output in op.output:
        outputs.append(op_output.name)

    # Find all controls
    controls = []
    for op_control in op.control_input:
        controls.append(op_control.name)

    # Add all nodes
    for op_input in op.input:
        if op_input.op.type == 'Placeholder':
            graph
