import weakref
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class QueueSet(object):
    """
    Interface Queue Set summary
    
    .. attribute:: nodes
    
    	List of nodes for which Queue\-set data is collected
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_oper.QueueSet.Nodes>`
    
    

    """

    _prefix = 'qos-ma-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = QueueSet.Nodes()
        self.nodes.parent = self

        self.yang_name = "queue-set"
        self.yang_parent_name = "Cisco-IOS-XR-qos-ma-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False

