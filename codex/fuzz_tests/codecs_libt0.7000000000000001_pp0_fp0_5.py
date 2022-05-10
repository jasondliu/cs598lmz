import codecs
codecs.open = open
import sys
import os
import re
import xml.dom.minidom
import xlrd
from xml.dom.minidom import parse
from xml.dom.minidom import parseString
from xml.dom.minidom import Document
from xml.etree.ElementTree import Element, SubElement, Comment, tostring,ElementTree
from xml.etree import ElementTree
from xml.etree.ElementTree import ParseError

def getNodeText(node):
    nodeText = ""
    for child in node.childNodes:
        if child.nodeType == node.TEXT_NODE:
            nodeText += child.data
    return nodeText

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False

def get_attrvalue(node, attrname):
    return node.getAttribute(
