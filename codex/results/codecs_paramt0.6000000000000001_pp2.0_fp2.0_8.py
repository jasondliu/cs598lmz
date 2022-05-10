import codecs
codecs.register_error('ignore', codecs.replace_errors)

# set up logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')

# find the directories we need
base_dir = os.path.abspath(os.path.dirname(__file__))
input_dir = os.path.join(base_dir, 'input')
output_dir = os.path.join(base_dir, 'output')

# create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# read the input files
input_files = os.listdir(input_dir)

# read the input files
input_files = os.listdir(input_dir)

# process each file in turn
for input_file in input_files:
    # create the output file name
    output_file = input_file.replace('.csv', '_clean.csv')
    output_file = os.
