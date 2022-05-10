import _struct
import time
from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka.errors import KafkaError

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.bind(('', 8899))

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

while True:
    print("Waiting for data...")
    data, addr = sock.recvfrom(1024)
    print("Got data from", addr)
    print("Data:", data.decode("utf-8"))
    producer.send('test', data)
    producer.flush()
