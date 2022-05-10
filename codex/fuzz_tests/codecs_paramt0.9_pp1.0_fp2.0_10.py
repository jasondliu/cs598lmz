import codecs
codecs.register_error("replace", codecs.lookup("iso-8859-15"))
#.decode('utf8', errors='replace')

class Graph(object):
    """
    main entity graph class
    """
    def __init__(self):

        self.nodes = dict() #map
        self.layers = dict()
        self.no_nodes = 0
        # self.bezeichner = dict()

    def build(self, layer_list):
        # self.nodes.clear()
        # self.layers.clear()

        for i in layer_list:
            self.add_layer(i)  ## TODO auch delete??
        ##################
        for n in self.layers:
            try:
                self.layers[n].build()
            except LayerException as e:
                # print(e)
                self.delete_layer(n)


    def get_node(self, name):
        for lay in self.layers:
            node = self.layers[lay].get_node(name)
            if node:
