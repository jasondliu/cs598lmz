import mmapi
import math
import os

# ------------------------------------------------------------------------------
def _set_translation(node, translation):
    '''
    Sets the translation of the given node.
    
    :Parameters:
        node : Node | str
            The node to set the translation of or the name of the node to set
            the translation of.
        translation : Point
            The translation to set on the node.
            
    :Return: The modified node.
    '''
    
    if(not isinstance(node, mmapi.Node)):
        node = mmapi.Structure.find(node)
    # Convert translation to numpy array
    translation = np.array(translation)
    # Set the translation on the node
    node.setTranslation(translation)
    return node

# ------------------------------------------------------------------------------
def _get_nodes_by_property(structure, prop):
    '''
    Returns a list of nodes in the structure with the given property.
    
    :Parameters:
        structure : Structure
            The structure to search.
        prop : str
            The property to look for.
    
    :Return
