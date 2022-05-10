import _struct
import _string
import _tree

class _DictValue:
    def __init__(self, value):
        self.value = value

class _DictCreateNode(object):
    def __init__(self, node):
        self.node = node
        
    def __getitem__(self, key):
        return _DictValue(_tree.TreeNode(self.node, key))
    
    def __setitem__(self, key, value):
        _tree.TreeNode(self.node, key).data = value
    
    def __contains__(self, key):
        return _tree.TreeNode(self.node, key).data != None
    
    def __delitem__(self, key):
        _tree.TreeNode(self.node, key).data = None

class _DictFromNode(object):
    def __init__(self, node):
        self.node = node
    
    def __getitem__(self, key):
        return self.node[key].data
    
