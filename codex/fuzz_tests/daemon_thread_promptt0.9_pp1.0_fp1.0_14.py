import threading
# Test threading daemon with a timeout

########################################################################################################################
# POOLERS

def daemon():
    threading.currentThread().isDaemon()
    return False

pooler = Pool(processes=4, initargs=[], initializer=daemon)

def limit(processed_count, limit_count=5, last_item=None):
    return last_item if processed_count >= limit_count else None

def get_result_list(pooler, generator, limit_count=5):
    result_list = []
    last_item = None
    while limit(len(result_list), limit_count):
        result = pooler.apply_async(generator, args=[last_item], callback=None, error_callback=None)
        result_list.append(result.get(timeout=5))
        last_item = result_list[-1]
    return result_list

########################################################################################################################
# Functions

def stop_generator(param=None):
    time.sleep(0.1)
    raise StopIteration

def stop_list(
