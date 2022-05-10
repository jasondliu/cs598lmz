import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

################################################################################

# Use the standard library to open the file, read it, and parse it as JSON.
import json
with open('../../data/ch02/usagov_bitly_data2012-03-16-1331923249.txt') as f:
    records = [json.loads(line) for line in f]

print(records[0])

################################################################################

# Count time zones in pure Python.
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
print(time_zones[:10])

################################################################################

# Count time zones using pandas.
import pandas as pd
frame = pd.DataFrame(records)
tz_counts = frame['tz'].value_counts()
print(tz_counts[:10])

################################################################################

# Fill in missing (empty) time zones with 'Missing'.
