import mmap

def convert(filenames, converter='convert', raw_type='SFCAIRS'):
    #
    # usage:
    #  convert(['filename'])
    #  convert(['filename1','filename2'...])
    #
    for filename in filenames:
        if "." not in filename: filename = filename + ".ascii"
        if not os.path.exists(filename):
            print("file " + filename + " does not exists!")
            continue
        output = filename.replace(".ascii","."+raw_type)
        # run external program
        call([converter, "-f", filename, "-o", output, "-t", raw_type])

if len(sys.argv) == 1:
    print("usage: convert.py file1 file2 ... filen")
    exit()

convert(sys.argv[1:])

#
# this part read the data
#
# ToDo: re-construct an API of the VNP library.
#

class Grid:
    def __init
