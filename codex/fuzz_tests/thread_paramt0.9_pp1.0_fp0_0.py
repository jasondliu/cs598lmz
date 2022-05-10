import sys, threading
threading.Thread(target=lambda: os.system('open "{}"'.format(sys.path[0]))).start()

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from xep_0059 import query
from xep_0059.fields import QueryField


def test_dont_query_root_node():
    document = query.Document()
    query_ = document.add_query('http://jabber.org/protocol/disco#items')
    node = query_.add_node('http://jabber.org/protocol/disco#info')
    node.add_identity(category='pubsub', type_='pep')
    node.add_feature('http://jabber.org/protocol/pubsub')
    node.add_feature('http://jabber.org/protocol/pubsub#meta-data')

    decoded_document, namespace = query.decode(document.to_string())
