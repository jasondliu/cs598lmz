import gc, weakref

#-----------ASN.1--------------#


#------------TLS config---------#
port = 2300

client_keys_path = "keys/key_client.pem"			# Client private key path
client_cert_path = "keys/cert_client.pem"			# Client public certificate path

CA_cert_path = "keys/cert_server.pem"			# Certification Authority public certificate path
CA_key_path = "keys/key_server.pem"				# Certification Authority private key

cipher = 'AES-256-CBC'						# Cipher used to encrypt data
hash_algorithm = "SHA256"					# Hash algorithm used to sign data

TLS_version = 'TLSv1.2'						# TLS version

hmac_digestmod = hashlib.sha256					# Digestmod used to to generate keys in TLS 1.2
#----------------------------------#

#-------------RSA config----------#
rsa_chunk_size = 200
