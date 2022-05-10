import socket

from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
from multiprocessing import Pool, cpu_count
from time import time
from paramiko import SSHClient, WarningPolicy, AuthenticationException, SSHException
from paramiko.ssh_exception import NoValidConnectionsError, BadHostKeyException, BadAuthenticationType
from paramiko.rsakey import RSAKey
from threading import Thread
from requests import get, post, exceptions
from json import loads
from os import path, mkdir

from delphos_config import distributed_machines, command, git_ssh_pub_key_path, passphrase, prod_id, prod_host, prod_port, prod_public_host, prod_public_port
from delphos_exceptions import get_error_message

from delphos_menus import *


# Creates a new user account, returning the username
#
# Machine hostname or IP: the machine where to create the account (default: localhost)
#
# Local user (username): the user account used to connect to the machine (optional
