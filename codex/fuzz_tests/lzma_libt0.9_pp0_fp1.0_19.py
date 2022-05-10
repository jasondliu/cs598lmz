import lzma
lzma.xz_config()

from subprocess import call
import sys
import socket

def sendData(data, connection):
    try:
        connection.send(data)
    except BrokenPipeError:
        pass

def readData(connection):
    message = ""
    while True:
        try:
            data = connection.recv(32768)
            if not data:
                break
            message += data.decode()
        except Exception as e:
            pass
    return message

def readAppsList(connection):
    apps = readData(connection)
    return json.loads(apps)

def readSizesList(connection):
    sizes = readData(connection)
    return json.loads(sizes)

# Json file template
"""
{
    "files": [
        {
            "id": "dNTfA_g.png",
            "source": "context_click_dNTfA_g.png"
        },
        {
            "id": "AiS9S9Y.png",
            "source
