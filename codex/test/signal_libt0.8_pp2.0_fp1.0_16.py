import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

import argparse

class EndToken:
    pass


# --- interface with dot ---

class Dot(object):
    @staticmethod
    def get_dot_graph(graph):
        """Make a graphviz dot graph from a graph.

        Parameters
        ----------
        graph : NetworkX graph
            The graph to convert.

        Returns
        -------
        dot_graph : string
            The graphviz dot representation of the graph.

        """
        return networkx.drawing.nx_pydot.to_pydot(graph).to_string()

    def __init__(self, graph):
        self._graph = graph
        self._dot_graph = self.get_dot_graph(graph)
        self._p = self._run_dot()

    def _run_dot(self):
        """Run dot and return its stdin, stdout, and stderr."""
