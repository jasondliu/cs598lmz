import threading
threading.stack_size(64*1024*1024)

def serialize():
    query_string = "select distinct st from station"
    cursor.execute(query_string)
    print("Serializing data...")
    os.remove("temp.pickle")
    stations = set()
    for (station,) in cursor:
        stations.add(station)
    with open("temp.pickle", "wb") as f:
        pickle.dump(stations, f)
    cursor.close()
    connection.close()
    print("Done serializing data.")


def find_identical_stations():
    connection = cx_Oracle.connect("scott/tiger@localhost/orcl")
    cursor = connection.cursor()
    query_string = "select distinct st from station"
    cursor.execute(query_string)
    print("Reading data from database!")
    stations = set()
    for (station,) in cursor:
        stations.add(station)
    print("Done reading data from database!")
    print("Finding identical stations.")
    with open("temp.
