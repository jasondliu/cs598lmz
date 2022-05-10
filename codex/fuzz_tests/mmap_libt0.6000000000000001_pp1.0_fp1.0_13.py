import mmap

#
# Global variables
#

#
# Functions
#
def extract_all_files(unpacked_data_dir, packed_data_dir):
    """
    Extracts all files in the packed_data_dir to the unpacked_data_dir.
    """
    for file_name in os.listdir(packed_data_dir):
        print("Extracting file: {0}".format(file_name))
        extract_file(unpacked_data_dir, packed_data_dir, file_name)

def extract_file(unpacked_data_dir, packed_data_dir, file_name):
    """
    Extracts a file from the packed_data_dir to the unpacked_data_dir.
    """
    packed_file_path = os.path.join(packed_data_dir, file_name)
    unpacked_file_path = os.path.join(unpacked_data_dir, file_name)

    # Create the unpacked file
    unpacked_file = open(unpacked_file_path, 'wb')
