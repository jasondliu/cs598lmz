import select
import socket
import json
import time
from pprint import pprint


META_DATA_URL = "http://metadata.google.internal/computeMetadata/v1/instance/"
ZONE = "zone"
PROJECT_ID = "project-id"
NETWORK = "network-interfaces"

def get_metadata(key):
    headers = {'Metadata-Flavor': 'Google'}
    url = META_DATA_URL + key
    req = urllib2.Request(url, None, headers)
    try:
        resp = urllib2.urlopen(req)
        return resp.read()
    except urllib2.URLError:
        return ""

def get_project_id():
    return get_metadata(PROJECT_ID)

def get_network_interfaces():
    return get_metadata(NETWORK)

def get_zone():
    return get_metadata(ZONE)

def get_instance_id():
    zone = get_zone().split("/")
    project_id = get_
