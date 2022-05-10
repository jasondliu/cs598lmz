import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Check if the current version of the file has been processed yet
def check_processed(filename):
	try:
		with open(filename) as processed_file:
			processed_version = processed_file.readline().strip()
			if processed_version == current_version:
				return True
			else:
				return False
	except:
		return False

# Remove the processed file if it exists
if os.path.exists(processed_filename):
	os.remove(processed_filename)

# Open the processed file for writing
processed_file = open(processed_filename, 'w')
processed_file.write(current_version + '\n')

# Load the CSV file
with open(csv_filename, 'r') as csv_file:
	reader = csv.DictReader(csv_file)
	
	# Loop through all the rows in the CSV file
	for row in reader:
		# Get the URL and
