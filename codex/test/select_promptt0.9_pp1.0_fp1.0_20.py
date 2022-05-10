import select
# Test select.select for read, write and exception
# events on STDIN.

readable, writable, exceptional = select.select([sys.stdin], [], [])



# SA ROLLOUT #
# - # First think about problem you are solving and then start coding!
# - # Keep the problem completely independent. Only code what is necessary to solve it!
#   # When working out pseudocode, the model: A - [B - C] is used.
# - # Define the possible A-C inputs and then model the B - C logic.

# Q. Model the following line of code:
a = 0

# A. [0] ---> [0]

# Q. Model the following line of code:
a = a + 1

# A. [0] ---> [0, +] ---> [1]

# Q. Model the following line of code:
a = a + 5

# A. [0] ---> [0, +] ---> [6]

# Q. Model the following line of code:
#    a = [1, 2, 3]
