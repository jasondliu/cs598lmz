import selectors
import socket
import ssl

import certifi
import urllib3

# This is an example of a Client / Server pair using SSL.
# The client requests the current time from the server by
# sending an empty payload. The server responds with an integer
# of the current epoch time in UTC.
#
# The server must have a certificate from a certificate authority
# for this example to work. You can either use a certificate from
# a well known authority or generate your own.
#
# To generate a certificate for your server do the following:
#
# 1. Generate a private key
#
# openssl genrsa -out server.key 2048
#
# 2. Generate a certificate signing request
#
# openssl req -new -sha256 -out server.csr -key server.key
#
# 3. Create a configuration file for the extensions
#
# vi extfile.cnf
#
# [req]
# distinguished_name = req_distinguished_name
# x509_extensions = v3_req
# prompt = no
# [req_distinguished_name]
