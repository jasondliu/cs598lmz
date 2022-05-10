import sys, threading

def run():
    global g_RabbitMQManager
    g_RabbitMQManager.ConsumeMessage()

def test():
    global g_RabbitMQManager
    g_RabbitMQManager.PublishMessage('Hello World!')

if __name__ == '__main__':
    g_RabbitMQManager = RabbitMQManager('192.168.1.10', 'guest', 'guest')
    threading.Thread(target=run).start()

    while True:
        test()
        time.sleep(1)
