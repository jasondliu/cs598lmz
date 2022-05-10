import ctypes
import ctypes.util
import threading
import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.io.sql import SQLTable
import getpass
from lxml import etree



def createPlant(plantID):
    global plantList
    plantList[plantID] = plant(plantID)
    print('init plant '+str(plantID)+' to plantList')
    return plantList[plantID]

def findPlant(plantName):
    for plantObj in plantList.values():
        if(plantObj.plantName == plantName):
            return plantObj
    return None

def findPlantByID(plantID):
    return plantList.get(plantID)

def getPlantIP(plantID):
    return findPlantByID(plantID).plantIP

# def itemizeTag(tagFull):
#     tagFullList = tagFull.split('/')
#     tagDict = {
#         'plant' : tagFullList[0],
#         'typeID' : tagFullList[1],

