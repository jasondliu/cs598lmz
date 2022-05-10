import threading
# Test threading daemon

def test_func():
    while True:
        print('test')
        time.sleep(1)

test_thread = threading.Thread(target=test_func)
test_thread.daemon = True
test_thread.start()

while True:
    print('main')
    time.sleep(1)

# Test threading for multiple requests to be sent using ThreadPoolExecutor
# The below code will send the requests in parallel and create a dictionary of all the responses

import concurrent
import threading

def test_func(request):
    # Send request and receive response
    return response

def main_func(requests):
    # Create a ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(requests)) as executor:
        # Create a dictionary of all responses
        responses = {executor.submit(test_func, request): request for request in requests}
        # Iterate over the responses and print them
        for future in concurrent.futures.as_completed(responses):
            response = future.
