import codecs
codecs.register_error('strict', codecs.ignore_errors)

def main():
    # Read in the file
    try:
        with open(sys.argv[1], 'r') as f:
            data = f.read()
    except:
        print("Could not open file: " + sys.argv[1])
        exit(1)

    # Parse the file
    try:
        data = json.loads(data)
    except:
        print("Could not parse file: " + sys.argv[1])
        exit(1)

    # Check for the correct version
    if data["version"] != 1:
        print("Unsupported version: " + str(data["version"]))
        exit(1)

    # Check for the correct type
    if data["type"] != "dictionary":
        print("Unsupported type: " + data["type"])
        exit(1)

    # Check for the correct format
    if data["format"] != "text/x-moz-place-container":
        print("Unsupported format: " + data["format"])

