import bz2
bz2.BZ2File(DATA_DIR+'wikidata-latest-all.json.bz2').read(10)

f = bz2.BZ2File(DATA_DIR+'wikidata-latest-all.json.bz2')
chunk_size = 1000
for i, line in enumerate(f):
    if i < chunk_size:
        print(line)
    else:
        break

import json
js = json.loads(line)
js.keys()

js['claims'].keys()

js['claims']['P31'][0]

js['claims']['P31'][0]['mainsnak']['datavalue']['value']['id']

js['claims']['P31'][0]['mainsnak']['datavalue']['value']['id'] == 'Q5'

js['claims']['P150'][0]['mainsnak']['datavalue']['value']['id']


