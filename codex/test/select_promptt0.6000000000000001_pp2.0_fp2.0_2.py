import select
# Test select.select() and select.poll()
import time

# Example of the select function

def run_select_example():
    input = [1,2,3]
    output = [1,2,3]
    error = [1,2,3]
    timeout = 2
    readable, writeable, exceptional = select.select(
        input, output, error, timeout
    )
