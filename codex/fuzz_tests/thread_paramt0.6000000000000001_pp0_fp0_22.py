import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

def main():

    # TODO: Implement the main function.

    # Objective:
    # 1. Parse the input file.
    # 2. Perform the algorithm.
    # 3. Write the output to a file.

    # 1. Parse the input file.

    # Read the input file.
    with open('queries.txt') as f:
        lines = f.readlines()

    # Get the number of queries.
    num_queries = int(lines[0])

    # Create a list of queries.
    queries = []
    for i in range(num_queries):
        # Get the number of names in the query.
        num_names = int(lines[1 + i * 3])
        # Get the names in the query.
        names = [line for line in lines[2 + i * 3].split('\n')[0].split(' ') if line]
        # Get the query.
        query = lines[3 + i * 3].split('\n')[0]
        #
