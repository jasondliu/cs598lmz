import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# Check if the current directory contains the "data" folder and if not, create it
if not os.path.isdir(os.path.join(os.getcwd(), "data")):
    os.mkdir(os.path.join(os.getcwd(), "data"))

# Check if the "data" folder contains the "raw" folder and if not, create it
if not os.path.isdir(os.path.join(os.getcwd(), "data", "raw")):
    os.mkdir(os.path.join(os.getcwd(), "data", "raw"))

# Check if the "data" folder contains the "processed" folder and if not, create it
if not os.path.isdir(os.path.join(os.getcwd(), "data", "processed")):
    os.mkdir(os.path.join(os.getcwd(), "data", "processed"))

# Check if
