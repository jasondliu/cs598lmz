import mmap
import csv


def main():
    # get the input file
    if len(sys.argv) > 1:
        inputFile = sys.argv[1]
    else:
        print("Usage: python3 parse.py <input file>")
        return

    # get the output file
    if len(sys.argv) > 2:
        outputFile = sys.argv[2]
    else:
        outputFile = "output.csv"

    # open the input file and read it into a bytearray
    with open(inputFile, 'rb') as f:
        data = bytearray(f.read())

    # open the output file for writing
    with open(outputFile, 'w', newline='') as csvFile:
        writer = csv.writer(csvFile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Time', 'Type', 'Address', 'Value', 'Data'])

        # parse the file
