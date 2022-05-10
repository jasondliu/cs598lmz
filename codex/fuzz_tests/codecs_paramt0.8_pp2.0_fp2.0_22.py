import codecs
codecs.register_error('dotreplace', codecs.lookup_error('replace'))

# SSP_max value from the training data set, used for scaling the safety vector
SSP_max = 20

# default values for the per-road-segment variables
default_speeds = {'motorway': 100, 'trunk': 80, 'primary': 70, 'secondary': 60, 'tertiary': 50, 'unclassified': 40, 'residential': 30, 'service': 20}
default_safety = {'motorway': 10, 'trunk': 10, 'primary': 10, 'secondary': 10, 'tertiary': 10, 'unclassified': 10, 'residential': 10, 'service': 10}

def parse_arguments():
    """
        parse arguments, see inline comments
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--out", help="Name of the output file")
    parser.add_argument("--osm", help="Name of the OSM file")
    parser.add_argument("--ways", help="Name of the
