import sys, threading
threading.Thread(target=lambda:sys.stdout.write('Hello from a background thread\n')).start()
"""

class Node:
    """
    Each node on the network is an instance of this object
    """

    node_counter = 0 # start with 0 count

    def __init__(self, network, node_id=None, node_type=Node.HUB, log=False, queued_packets=[], id_prefix='N'):
        # the global counter of nodes
        Node.node_counter += 1

        # node_type = CHHUB, RSU, VEHICLE, V2V, V2I
        # node_id: unique id of the node (int)
        # external_id: more descriptive than node_id, e.g. 'L1C1' (string)
        # network: belongs to which network (Network)

        self.node_type = node_type

        if node_id == None:
            node_id = Node.node_counter
        self.node_id = node_id

        self.network = network
        self.id_prefix = id_
