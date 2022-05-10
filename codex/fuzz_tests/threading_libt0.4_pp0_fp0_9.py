import threading
threading.stack_size(67108864)

def get_data_from_url(url):
    try:
        #print("get_data_from_url",url)
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        print("get_data_from_url",e)
        return None

def get_data_from_file(file_name):
    try:
        with open(file_name, "r") as f:
            return json.load(f)
    except Exception as e:
        print("get_data_from_file",e)
        return None

def get_data_from_url_with_retry(url):
    try:
        data = get_data_from_url(url)
        if data is None:
            time.sleep(1)
            data = get_data_from_url(url)
            if data is None:
                time.sleep(1)
                data =
