import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# Define the path to the CSV file
path = "C:/Users/david/Desktop/Python/Data/Data.csv"

# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(path, 'r') as text:
    # Store all of the text inside a variable called "text"
    text = text.read()

# Split the text on the newline character ('\n') and store the resulting list in "rows"
rows = text.split('\n')

# Store the first row of the list in "header"
header = rows[0]

# Store the rest of the rows in "data"
data = rows[1:]

# Create a for loop to print out each row
for datum in data:
    # Print out the row
    print(datum)

# Create a for loop to print out each row
for datum in data:
    # Split the row on commas and
