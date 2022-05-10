import threading
threading.stack_size(67108864)

def start_mining():
    while True:
        if get_state() == 'mining':
            r = requests.post('http://127.0.0.1:5000/mine_block', json={'address': address})
            if r.status_code == 200:
                print('Block mined!')
            else:
                print('Error:', r.status_code)
        time.sleep(2)


def start_node(address, port):
    node_id = str(uuid4()).replace('-', '')
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/node-' + str(node_id)

    mongo = PyMongo(app, config_prefix='MONGO')
    db = mongo.db

    db.my_wallet.insert_one({
        'address': address
    })

    db.transactions.create_index([('hash', pymongo.ASCENDING)], unique=True)
