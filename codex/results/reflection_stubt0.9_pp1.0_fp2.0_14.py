fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# Scrapes the provided key with options
def scrape(key, option):
    print('[!] Requested: ', key)

    # Send a HEAD request to check if the ID exists in the database
    try:
        r = requests.head(url + key + '.json')
    except requests.exceptions.RequestException as e:
        print('[!] Also found:', e)

    # Valid ID -- Attempt extraction
    if r.status_code == 200:

        print('[!] Found ' + key + ' ...downloading')

        # Download the JSON from the database
        ack_json = (requests.get(url + key + '.json').text)

        # Converts the JSON string into a Python dictionary

        if (option == "all"):
            # Converts the JSON string into a Python dictionary
            ack_dict = json.loads(ack_json)
            ack_dict_all = ack_dict

            # Converts the Python dictionary (ack_dict) into a CSV object
            ack_csv = csv.DictWriter(open('out
