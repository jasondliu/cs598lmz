import lzma
lzma.decompress(b'YmF2YQ==')

# zlib
import zlib
zlib.decompress(b'YmF2YQ==')

# bz2
import bz2
bz2.decompress(b'FZQQoNwAHe5D5k/uJ3qrcp7XeBDvx8+7VYTA2fRgkVlIogZ8n+ZgPMjQU=')


# =================================================================================================================
# MIME message
# =================================================================================================================

# SinglePart
import email
msg = email.message_from_string('From: foo@example.com\r\nSubject: class\r\n\r\nMy message')
msg.items()
msg.get_content_type()
msg.get_param('subject')
msg.get('From')
msg.get_payload()  # only get text, not MIME object
msg.get_payload(decode=True)  # get MIME object, may raise "DecodingError"

#
