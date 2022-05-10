import sys, threading

def run():
    subprocess.Popen(["python3.5", "Mqtt_Kafka_relay.py"],
                     stdout=-1,
                     stderr=-1,
                     stdin=-1)

threads = []
while True:
    subprocess.call(["python3.5", "Mqtt_Kafka_relay.py"])
</code>

