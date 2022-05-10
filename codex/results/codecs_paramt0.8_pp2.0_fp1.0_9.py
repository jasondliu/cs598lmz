import codecs
codecs.register_error('ignore', codecs.lookup_error('ignore'))
import os
import re

def main():

    filePath = "D:\\Code\\dbpedia\\"

    fileList = os.listdir(filePath)

    for f in fileList:
        print(f)
        file = open(filePath + f, 'r', encoding='ISO-8859-1')
        file.readline()

        idx = 1
        outPath = "D:\\Code\\dbpedia\\dbpedia_split\\"
        outFile = open(outPath + f, 'w', encoding='utf-8')

        while True:
            line = file.readline()
            if line.strip() == "":
                if idx % 1000 == 0:
                    outFile.close()
                break
            if idx % 1000 == 0:
                outFile.close()
                outFile = open(outPath + str(idx) + "_" + f, 'w', encoding='utf-8')
            outFile.write(line)
            idx = idx + 1

if
