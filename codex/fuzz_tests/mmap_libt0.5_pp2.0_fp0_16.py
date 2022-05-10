import mmap
import re
import sys

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", required=True, help="File to search")
    parser.add_argument("-r", "--regex", required=True, help="Regex to search for")
    parser.add_argument("-g", "--group", required=True, help="Group to output")
    return parser.parse_args()

def main():
    args = get_arguments()
    try:
        with open(args.file, "rb") as f:
            mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
            for match in re.finditer(args.regex, mm):
                print(match.group(int(args.group)))
    except IOError as e:
        print("File not found: {}".format(e))
        sys.exit(1)
    except ValueError as e:
        print("Invalid regex: {}".format(e))

