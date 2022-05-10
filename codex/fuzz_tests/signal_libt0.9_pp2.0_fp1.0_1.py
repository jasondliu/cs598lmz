import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

# File Settings
NUM_STARS = -1
NUM_IMAGES = -1
FILE_INPUT = 'testset/images/sdss'
FILE_OUTPUT = 'testset/images/csv/data'
RESOLUTION = '64'
OVERWRITE_CSV = False

def create_data(value_list):
    data_set = {}
    for i in range(len(value_list)):
        data_set[filename_list[i]] = {
            'ra': value_list[i][0], 
            'dec': value_list[i][1],
            'redshift': value_list[i][2]
        }
    return data_set

def write_csv(data_set, file_name, csv_file):
    with open(csv_file, 'a') as csvfile:
        csvfile_name = file_name.replace('.fits', '.jpg') + '.csv'
        star_writer = c
