import threading
threading.stack_size(67108864)

def lambda_handler(event, context):
    ret = get_flights()
    print(ret)
    return {
        'statusCode': 200,
        'body': json.dumps('Done')
    }

def get_flights():
    payload = {'apikey': AIRPORT_API_KEY}
    r = requests.get(AIRPORT_API_ENDPOINT, params=payload)
    airports = r.json()
    print(airports)

    airports_to_process = []
    for airport in airports:
        payload = {'airport': airport['icao']}
        r = requests.get(FLIGHT_API_ENDPOINT, params=payload)
        flights = r.json()
        airports_to_process.append((airport, flights))

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(process_airport, airports_to_process)

def process_airport(airport
