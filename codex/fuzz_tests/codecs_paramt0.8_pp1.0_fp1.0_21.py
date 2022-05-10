import codecs
codecs.register_error('replace_and_asciify', replace_and_asciify)

def getFiledList(inputFile):
    # if inputFile is unicode, encode it to utf-8 to open
    inputFileUTF8 = inputFile
    if type(inputFile) == unicode:
        inputFileUTF8 = inputFile.encode('utf-8')
    f = open(inputFileUTF8, "r")
    tsvReader = csv.reader(f, delimiter='\t')
    return tsvReader.next()

def getFiledDict(inputFile):
    filedList = getFiledList(inputFile)
    filedDict = {}
    i = 0
    for value in filedList:
        filedDict[value] = i
        i = i + 1
    return filedDict

def getDictReader(inputFile, fieldDict):
    inputFileUTF8 = inputFile
    if type(inputFile) == unicode:
        inputFileUTF8 = inputFile.encode('utf-8')
    f = open(inputFile
