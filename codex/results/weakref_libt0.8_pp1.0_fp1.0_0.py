import weakref

from toolbox.bitstream import BitStream
from toolbox.pairinggroup import G1,ZR,pair
from toolbox.element import serialize, deserialize
from toolbox.PKSig import PKSig
from toolbox.iterate import dotprod
from toolbox.symcrypto import AuthenticatedCryptoAbstraction
from toolbox.conversion import Conversion

from tau17 import tau17
from charm.engine.util import *
import sys, random, string
from toolbox.pairinggroup import *

class CPabe09_BSW07(PKSig):
    def __init__(self):
        global group, debug
        debug = False
        group = PairingGroup('SS512')
        pass

    def setup(self):
        global g1, g2
        g1 = group.random(G1)
        g2 = group.random(G1)
        alpha = group.random()
        gpk = { 'g1':g1, 'g2':g2, 'g2_alpha':g2 ** alpha }
        g
