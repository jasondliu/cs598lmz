import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

# Open the CSV file with the data
file_name = 'screens.csv'
data_file = list(csv.reader(open(file_name, "r", encoding='utf-8'), delimiter=","))

# Initialize the variables
total_number_of_screens = 0
number_of_screens_with_results = 0
number_of_screens_that_run = 0
number_of_screens_that_have_certain_results = 0

# Loop through the data
for row in data_file:

    # Convert the variables to integers
    number_of_plates = int(row[3])
    number_of_replicates = int(row[4])
    
    # Number of screens increases by one
    total_number_of_screens = total_number_of_screens + 1

    # Check if the screen ran
    if number_of_plates > 0:
        # Add one to the counter if it did
       
