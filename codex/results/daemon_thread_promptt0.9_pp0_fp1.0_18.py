import threading
# Test threading daemon
def runner(divid, session):
    global results
    global finished
    try:
        result = session(divid)
        results[divid] = result
        finished += 1
        print "%s: Finished %s" % (divid, result)
    except Exception as e:
        results[divid] = e
        finish += 1
        print "%s: Finished with error %s" % (divid, e)


def create_cust_data(divid):
    """ Returns random customer data """
    suffixes = ['aa', 'ab', 'ac', 'ad']
    return {
        "name": "%s %s" % ('John', random.choice(suffixes)),
        "customer_id": divid
    }

async_threads = []
for i in range(16):
    print "Setting up %s" % i
    thread = threading.Thread(target=runner, args=(i, create_cust_data))
    thread.daemon = True
    thread.start()
    async_threads.append(thread)


