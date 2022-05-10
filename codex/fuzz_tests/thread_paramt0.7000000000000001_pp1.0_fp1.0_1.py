import sys, threading
threading.Thread(target=lambda:sys.stdout.write('\n')).start()

# Convert .xlsx file to .csv
#!python3.7 xlsx2csv.py excel.xlsx -o excel.csv
 
# https://stackoverflow.com/questions/16503560/read-specific-columns-from-csv-file-with-csv-module
# Define the names of the columns that you want to extract
columns = ['Name', 'City', 'Age', 'Profession']
# Open the CSV file and load the contents into your program
with open('excel.csv') as csv_file:
    # Create a csv.DictReader object from the file
    csv_reader = csv.DictReader(csv_file)
    # Create a new list object to hold the selected columns
    selected_columns = []
    # Loop through the columns in the current row of the CSV file
    for row in csv_reader:
        # Create a dictionary to hold the values of the columns we want
        selected_row = {}
        # Loop through each column in
