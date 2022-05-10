import threading
threading.stack_size(1024*1024) # set stack size to be 1024MB

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
def reverse(head):
    # Implement this placeholder.
    return None


from test_framework import test_utils_generic_main, test_utils

if __name__ == '__main__':
    test_utils_generic_main.generic_test_main('reverse_sublist.tsv', reverse)
