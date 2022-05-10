import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

# Set the current working directory to the script directory
current_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_directory)

# Load the input files
input_directory = './input'
input_files = os.listdir(input_directory)
input_files.sort()

input_file_count = len(input_files)
if input_file_count == 0:
    print('No input files found.')
    sys.exit(0)

# Load the input files into a list
input_file_list = []
for file in input_files:
    input_file_list.append(os.path.join(input_directory, file))

# Define the variables
counter = 0
output_directory = './output'

# Check if the output directory exists. If not, create it.
if not os.path.exists(output_directory):
    os.mkdir(output_directory)

# Create a
