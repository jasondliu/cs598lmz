import _struct
from binascii import hexlify
from py_ecc.bls import privtopub, sign, verify
from py_ecc.optimized_bls12_381 import (
    G1, multiply,
    field_modulus,
)
from solana.rpc.api import Client

BACHET_PRIV = (
    "1111111111111111111111111111111111111111111111111111111111111111"
)

BACHET_PUB = (
    "039e078a17e27c7d90e2cfcc6b2cdaadbea6c92e6d957b7c8b1a55b7e5f5eac0af"
)

IANCOLE_PRIV = (
    "2222222222222222222222222222222222222222222222222222222222222222"
)

