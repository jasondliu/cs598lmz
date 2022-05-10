import _struct
from binascii import hexlify, unhexlify
from util import utxo_from_json, utxo_from_txid, utxo_from_txid_n,\
    find_utxo_index, find_utxo_indexes, find_utxo_indexes_for_address,\
    build_op_return, send_tx, build_native_p2wpkh, build_p2pkh,\
    build_native_p2wsh, build_tx_from_utxos

def test_utils():
    print("Testing utils")

    raw_utxos = open('./tests/raw_utxos.json', 'r').read()

    utxos_from_file = json.loads(raw_utxos)
    for utxo in utxos_from_file:
        utxo['value'] = int(utxo['value'], 16)
        utxo['scriptPubKey'] = unhexlify(utxo['scriptPubKey'])

    tx
