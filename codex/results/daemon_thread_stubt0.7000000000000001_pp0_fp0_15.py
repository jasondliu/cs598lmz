import sys, threading

def run():
    if len(sys.argv) == 1:
        print("Usage: python %s <port> <test_file_path> <expected_output_file_path>" % __file__)
        return

 
