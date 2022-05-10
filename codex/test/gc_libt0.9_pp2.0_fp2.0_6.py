import gc, weakref

class Tree(object):
    '''
    classdocs
    '''

    def __init__(self, parent, branch_length, id_prefix=''):
        self.parent = parent
        self.branch_length = branch_length
        self.left = None
        self.right = None
        self.id = None
        self.state = None
        self.id_prefix = id_prefix
        self.data = {}
        
    def leaf_ids(self):
        '''
        Leaves ids in the tree from left to right.
        '''
        if self.isLeaf():
            return [self.id]
        else:
            return self.left.leaf_ids() + self.right.leaf_ids()
    
    def lca(self, ids):
        '''
        Returns LCA node in the tree with
        each of the given `ids` a descendant.
        '''
