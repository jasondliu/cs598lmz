import codecs
codecs.register_error('strict', codecs.ignore_errors)

# check if the file exists
def fileExists(file):
    return os.path.isfile(file)

# create a file
def createFile(file):
    if not fileExists(file):
        # create a file
        open(file,"w").close()

# read a file
def readFile(file):
    # check if the file exists
    if fileExists(file):
        # open the file
        with open(file, "r") as f:
            # read the content
            content = f.read()
        # return the content
        return content
    else:
        return None

# write a file
def writeFile(file, content):
    # open the file
    with codecs.open(file, "w", "utf-8") as f:
        # write the content
        f.write(content)

# append a file
def appendFile(file, content):
    # open the file
    with codecs.open(file, "a", "utf
