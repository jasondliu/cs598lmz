import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
        cursor.execute("INSERT INTO test.randoms (random) VALUES (%s)", [random.random()])
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)

if __name__ == "__main__":
    signal.signal(signal.SIGALRM, handler)
    handler()
    connection_parameters = {
        "host":       "localhost",
        "port":       5432,
        "database":   "test",
        "user":       "postgres",
        "password":   "postgres",
    }
    connection = psycopg2.connect(**connection_parameters)
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE test.randoms (random REAL)")
    signal.pause()
