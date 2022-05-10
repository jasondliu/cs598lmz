import gc, weakref

def _default_action(resolver, action_hello_world):
    return None
    
def _node_new(_node_class, init_args, action, source_attrs):
    return None
        
def _node_new_from_attribute(_node_class, action, source_attrs):
    return None
    
#=========================================================================#
# Register/Unregister test
#=========================================================================#
class TestRegisterUnregister(unittest.TestCase):
    def setUp(self):
        self.graph0 = NodeGraph()
        self.graph1 = NodeGraph()
        self.graph2 = NodeGraph()
        self.graphs = [self.graph0, self.graph1, self.graph2]
        
    def test_register(self):
        class MyNodeClass(NodeBase):
            pass
        
        my_node = MyNodeClass()
        
        # In case of register, the class must be in graph's nodes
        self.assertFalse(MyNodeClass in self.graph0.nodes)
        self.graph0.register(MyNode
