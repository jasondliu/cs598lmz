import gc, weakref, os

from kupu.plone import uuidToObject
from kupu.plone.interfaces import IKupuContextMenuSupport
from kupu.plone.interfaces import IKupuLinkHandler
from kupu.plone.interfaces import IKupuStyleMapping

from kupu.plone.objects import KupuLinkHandler, KupuContextMenuSupport


def _compareVersion(compversion, currentversion):
    """ check if compversion is greater than or equal to currentversion """

    # check if a comparison string is given
    if compversion is None:
        # if not, the compare function returns 'True'
        return True
    # prepare a array of integers from the given version
    compversion = [int(x) for x in compversion.split('.')]
    currentversion = [int(x) for x in currentversion.split('.')]
    # iterate through the version components and compare

    second_break = False
    for i in range(0, len(compversion)):
        if compversion[i] >
