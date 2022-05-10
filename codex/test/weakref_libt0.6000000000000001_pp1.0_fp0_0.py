import weakref

from pymt.graphx.node import MTNode, MTNodeEvent
from pymt.graphx.event import MTGraphEvent
from pymt.graphx.edge import MTEdge, MTEdgeEvent
from pymt.graphx.graph import MTGraph
from pymt.graphx.utils import get_topological_sort
from pymt.graphx.node import MTNodeBinding

__all__ = ('MTGraphExecutor', )


class MTGraphExecutor(MTNode):
    def __init__(self, *largs, **kwargs):
        super(MTGraphExecutor, self).__init__(*largs, **kwargs)
        self.bind(on_node_event=self._on_node_event)
        self.execution_graph = MTGraph()
