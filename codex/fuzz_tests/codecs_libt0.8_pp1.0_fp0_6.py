import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)
def printToConsole(self, msg):
    codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)
    print(msg)


def print2Console(msg):
    print(msg)


def write2File(fName, msg):
    with open(fName, "a+") as myfile:
        myfile.write(msg + "\n")


def printToFile(fName, msg):
    print2Console(msg)
    write2File(fName, msg)


data_path = 'C:\\Users\\hankai\\Desktop\\data\\'
# data_path = 'D:\\pythonworkspace\\'
target_path = 'D:\\pythonworkspace\\'
# target_path = 'C:\\Users\\hankai\\Desktop\\data\\'


def readOutFile(fName):
    try:
        with open(fName, 'r', encoding
