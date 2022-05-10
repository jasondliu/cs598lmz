import codecs
codecs.register_error('surrogatepass', codecs.surrogateescape)
datestring = datetime.datetime.today().strftime("%Y%m%d")
coeff = 100000 #arbitrary scaling factor, should come from metadata

for file_name in ['STARTER', 'COMPARISON']:

    offset = 0.0 #arbitrary offset (probably unnecessary)
    basename = os.path.splitext(file_name)[0]
    input_file = os.path.join(os.getcwd(), file_name)
    output_file = os.path.join(os.getcwd(), basename+'_SWIPE_'+ datestring + '.csv')
    header = None

    #open source file, read all lines
    with open(input_file, 'rU') as csvfile:
        reader = csv.reader(csvfile)

        #get start/stop hours from header lines in metadata
        for row in reader:
            if row[0].startswith('TIME'):
                start_hour = int(row[1])

