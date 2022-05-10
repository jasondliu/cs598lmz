import sys, threading
threading.Thread(target=lambda: __import__('time').sleep(900000000)).start()
sys.path.append('lib')
sys.path.append('src')
sys.path.append('../src')

import json, os, pprint, pytest, rdflib, requests, urllib.parse, vcr
from rdflib import URIRef, Graph

from .common import get_test_config, test_namespace
from .common import test_collection_id, test_anno_id, test_layer_id, test_layer_name, test_layer_type
from .common import test_anno_id2, test_anno_layer_id, test_anno_layer_name, test_anno_layer_type

from annofabapi.models import Department, ProjectMemberRole, ProjectMember

from annofabcli.common.cli import (
    ArgumentParser,
    build_annofabapi_resource_and_login,
    get_json_from_args,
    get_wait_options_from_args,
    MainCommand,
)
