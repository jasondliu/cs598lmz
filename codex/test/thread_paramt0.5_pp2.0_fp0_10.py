import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

# Read input from STDIN
lines = sys.stdin.readlines()

# Print output to STDOUT
for line in lines:
    print(line.strip())

# Write output to STDERR
for line in lines:
    sys.stderr.write(line)

# Sample code to read in test cases:

import sys
test_cases = open(sys.argv[1], 'r')
