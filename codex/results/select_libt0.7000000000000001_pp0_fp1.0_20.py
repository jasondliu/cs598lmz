import select
from scapy.all import *
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import AES, PKCS1_OAEP


def send_message(s, message):
    # Encode message to bytes, prepare header and convert to bytes, like for username above, then send
    message = message.encode('utf-8')
    header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
    message = header + message
    s.send(message)


def encrypt_message(message, private_key):
    private_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(private_key)
    encrypted_message = cipher.encrypt(message)
    return encrypted_message


def decrypt_message(encrypted_message, public_key):
    public_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(public_key)
    message = cipher.decrypt(encrypted_message)
    print(
