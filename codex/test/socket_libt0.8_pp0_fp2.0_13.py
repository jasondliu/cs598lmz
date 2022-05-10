import socket
import threading
import time

from kubernetes import config
from kubernetes import client
from kubernetes.client.rest import ApiException
from kubernetes.stream import stream

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter(
    '[%(asctime)s] %(levelname)s in %(module)s: %(message)s')
ch.setFormatter(formatter)
log.addHandler(ch)

group = 'databases.example.com'
name = 'postgres-standalone'
version = 'v1'
plural = 'postgreses'

appname = 'postgres-standalone'

def on_create(configmap):
    log.info(configmap.metadata.name)
    configmap_data = configmap.data
