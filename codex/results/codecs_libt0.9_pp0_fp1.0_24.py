import codecs
codecs.getwriter('utf-8')(sys.stdout)

# start by parsing the command line
parser = argparse.ArgumentParser(description='Script to import elements from an osm file into a graph visualization')
parser.add_argument('osm_file', help='path to osm file')
parser.add_argument('out_file', help='path to the output file')

# add optional arguments
parser.add_argument('--lon', '-lon', help='center longitude', default=13.383333)
parser.add_argument('--lat', '-lat', help='center latitude', default=52.516667)
parser.add_argument('--zoom', help='zoom level', default=15)
parser.add_argument('--tags', help='additional tags to be visualized', nargs='+', default="")

args = parser.parse_args()


lon_center = args.lon
lat_center = args.lat
zoom = args.zoom
tags = args.tags
print(tags)

import_file = args.osm_file

