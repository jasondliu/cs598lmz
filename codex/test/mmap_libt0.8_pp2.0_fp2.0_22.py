import mmap
import sys
import json

def getTime(line):
    start = line.find("@")
    if start == -1:
        return None
    end = line.find("]", start)
    if end == -1:
        return None
    timeStr = line[start + 1:end]
    timeStamp = time.mktime(time.strptime(timeStr, "%Y-%m-%d %H:%M:%S"))
    return timeStamp

def getJson(line):
    start = line.find("{")
    if start == -1:
        return None
    end = line.rfind("}")
    if end == -1:
        return None
    return line[start:end+1]

# def getJson(line):
#     start = line.find("{")
#     if start == -1:
#         return None
#     # end = line.rfind("}")
#     # if end == -1:
#     #     return None
#     return line[start:]


