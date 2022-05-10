import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

def readFile(fileName):
    with open(fileName, "r", encoding='utf-8', errors='ignore') as file:
        return file.read()

def writeFile(fileName, content):
    with open(fileName, "w", encoding='utf-8') as file:
        file.write(content)

def readFileByLine(fileName):
    with open(fileName, "r", encoding='utf-8', errors='ignore') as file:
        return file.readlines()

def writeFileByLine(fileName, content):
    with open(fileName, "w", encoding='utf-8') as file:
        file.writelines(content)

def readFileByLineList(fileName):
    return [line.rstrip('\n') for line in open(fileName)]

def readFileByLineSet(fileName):
    return set(line.rstrip('\n') for line in open(fileName))
