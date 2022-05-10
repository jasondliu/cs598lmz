import lzma
lzma.LZMAFile()
lzma.open()

import statistics
statistics.STAT_TABLE_SIZE

import ssl
ssl.SSLObject
ssl.SSLSocket
ssl.create_default_context()
ssl.create_default_context().load_cert_chain()
ssl.create_default_context().load_dh_params()
ssl.create_default_context().load_dh_params("foo")
ssl.create_default_context().load_dh_params(b"foo")
ssl.create_default_context().load_verify_locations()
ssl.create_default_context().load_verify_locations("foo")
ssl.create_default_context().load_verify_locations("foo", "bar")
ssl.create_default_context().protocol
ssl.create_default_context().protocol = ssl.PROTOCOL_TLSv1
ssl.create_default_context().verify_mode
ssl.create_default_context().verify_mode = ssl.CERT_OPTIONAL
ssl.create_default_context
