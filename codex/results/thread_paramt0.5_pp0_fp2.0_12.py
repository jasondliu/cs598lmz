import sys, threading
threading.Thread(target=lambda: sys.stdin.readline()).start()
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def find_path(root, sequence):
    # TODO: Write your code here
    if root is None:
        return len(sequence) == 0
    return find_path_recursive(root, sequence, 0)

def find_path_recursive(current_node, sequence, sequence_index):
    if current_node is None:
        return False

    sequence_length = len(sequence)
    if sequence_index >= sequence_length or current_node.value != sequence[sequence_index]:
        return False

    if current_node.left is None and current_node.right is None and sequence_index == sequence_length - 1:
        return True

    return find_path_recursive(current_node.left, sequence, sequence_index + 1) or \
           find_path_recursive(current_node.right, sequence, sequence
