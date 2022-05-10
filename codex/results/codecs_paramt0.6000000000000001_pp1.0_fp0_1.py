import codecs
codecs.register_error("ignore", codecs.ignore_errors)

# Read in from stdin
# ==================

# Get the input and split it into lines
input = sys.stdin.read()
input = re.split("\n", input)

# Remove all empty lines
input = [x for x in input if x != ""]

# Get the number of lines of input
n = int(input[0])

# Process each line of input
# ==========================

# Initialize the list of output lines
output = []

for i in range(1, n+1):
    # Get the number of words in the line
    m = int(input[i])

    # Get the words
    words = input[i+1:i+m+1]

    # Get the number of the test case
    case = i/float(n)

    # Get the answer
    answer = solve(words)

    # Make the output line
    output.append("Case #%d: %s" % (case, answer))

# Print to stdout
# ===============

# Print the
