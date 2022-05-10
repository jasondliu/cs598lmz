from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(frame.value)
 

# In[ ]:

from kafka import SimpleProducer, KafkaClient
import json
from pymongo import MongoClient
import re
from lxml import etree
from lxml.etree import XMLSyntaxError
from datetime import datetime


# In[ ]:

def get_topic_offset(topic, kafka_client):
    """
    Get the offset of the latest message on the topic.
    """
    topic_partitions = kafka_client.get_topic_partitions(topic)
    partition = topic_partitions[0].partition
    topic_offset = kafka_client.get_simple_consumer(topic, 0, auto_commit=True).offsets[partition]
    latest_offset = topic_offset[-1]
    return latest_offset


# In[ ]:

def get_message_from_topic(topic, kafka_client, start_offset=0, max_messages=10):
    """
    Get a specified number of messages from the topic starting
