import gc, weakref

from charm.schemes.abenc.abenc_bsw07 import CPabe_BSW07
from charm.toolbox.pairinggroup import PairingGroup,ZR,G1,G2,GT,pair
from charm.toolbox.ABEnc import ABEnc, InputError
from charm.core.math.integer import integer,randomBits
from charm.core.crypto.cryptobase import *

debug = False
class CPABE_BO11(ABEnc):
    """
    >>> from charm.toolbox.pairinggroup import PairingGroup,GT
    >>> from charm.toolbox.ABEncMultiKey import ABEncMultiKey
    >>> group = PairingGroup('SS512')
    >>> abe = CPABE_BO11(group)
    >>> (master_public_key, master_key) = abe.setup()
    >>> f = open('mpk.charmPickle', 'wb')
    >>> master_public_key.serialize(f)
    >>> f.close()
    >>> f = open('msk.charmPickle', 'wb
