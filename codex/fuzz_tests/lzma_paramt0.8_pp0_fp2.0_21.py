from lzma import LZMADecompressor
LZMADecompressor().decompress(b'x\x9c\xcbH\xcd\xc9\xc9W(\xcf/T\xcaI\x01\x00\xd1\xa8\x04\xf0')

"""
"""
# FONTS
from matplotlib import font_manager
print([f.name for f in font_manager.fontManager.ttflist])

"""

"""
# KAFKA
import json
from kafka import KafkaProducer
import time
producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('python-topic', json.dumps({'time': time.time()}).encode('utf-8'))
producer.flush()

from kafka import KafkaConsumer
consumer = KafkaConsumer('python-topic', bootstrap_servers='localhost:9092')
for record in consumer:
    print(record)

"""

"""
# LINUX
# listar processos
os.system('top')

# listar arquivos
os.system('ls
