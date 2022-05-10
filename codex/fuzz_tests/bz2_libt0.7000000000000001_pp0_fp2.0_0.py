import bz2
bz2.BZ2File('a.bz2').read()

# https://stackoverflow.com/questions/30422202/how-to-save-a-bz2-file-in-python-without-reading-it-fully-in-memory
# https://regex101.com/r/oH8tO1/1
import requests
import bz2
r = requests.get('https://transfer.sh/9XFtZ/testfile.bz2')
with bz2.BZ2File('testfile.bz2', 'wb') as f:
    f.write(r.content)

# https://stackoverflow.com/questions/30422202/how-to-save-a-bz2-file-in-python-without-reading-it-fully-in-memory
# https://regex101.com/r/oH8tO1/1
import requests
import bz2
r = requests.get('https://transfer.sh/9XFtZ/testfile.bz2')
with bz2
