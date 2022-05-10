import threading
threading.stack_size(100000000) # Increase stack size so that the error "thread stack overflow" doesn't occur

def get_node_by_id(nodes, node_id):
    """
    Returns the node with the given id.
    """
    for node in nodes:
        if node.get_id() == node_id:
            return node
    return None

def remove_constraint(a, b, constraints):
    for constraint in constraints:
        if a in constraint and b in constraint:
            constraints.remove(constraint)

def check_constraints(constraints_list, domain_list1, domain_list2):
    """
    Checks if two lists of domains satisfy all constraints.
    """
    for i in range(len(domain_list1)):
        for j in range(i+1, len(domain_list1)):
            if domain_list1[i] == domain_list2[j] and domain_list1[j] == domain_list2[i]:
                if (domain_list1[i], domain_list
