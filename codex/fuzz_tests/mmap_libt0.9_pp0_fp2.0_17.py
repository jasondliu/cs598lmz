import mmap # For arbitrary percision
from M2Crypto import BIO, Rand, SMIME, X509
from email.parser import Parser
from email.mime.text import MIMEText
from email.MIMEMessage import MIMEMessage
from email import message_from_string
import email.charset
import base64
import zlib

class M2CryptoError(Exception): pass

class utility:
    @staticmethod
    def sign(cert, key, input):
        email.charset.add_charset('utf-8',email.charset.QP,email.charset.QP, 'utf-8')
        s = SMIME.SMIME()
        s.load_key_bio(BIO.MemoryBuffer(cert), BIO.MemoryBuffer(key))

        # convert string input to an email object
        message = MIMEMessage(message_from_string(input))

        if isinstance(message, MIMEMessage):
            data = message.fp.getvalue()
        else:
            data = message.as_
