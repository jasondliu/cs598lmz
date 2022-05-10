import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

# Define a function that prints the data as a table
def print_table(data):
    # Determine the length of each column
    max_lengths = [len(str(v)) for v in data[0]]
    for row in data:
        for i, v in enumerate(row):
            max_lengths[i] = max(max_lengths[i], len(str(v)))
    # Generate the format string
    format_string = ''
    for i, v in enumerate(max_lengths):
        format_string += '{' + str(i) + ':' + str(v) + '} '
    format_string += '\n'
    # Print the data
    for row in data:
        print(format_string.format(*row))

# Define a function that clears the screen
def clear():
    print('\x1b[2J\x1b[H', end='')

# Define a
