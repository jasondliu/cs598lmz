import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()
# [END boolean_contains]

# [START string_contains_METHOD]
# ./cloud-client-library-code-snippets/python/keyword/string_contains_METHOD.py
from google.cloud import firestore

# Create a Firestore client.
db = firestore.Client()

# Filter for documents where a field contains a string.
users_ref = db.collection(u'users')
query = users_ref.where(u'name', u'==', u'Ada Lovelace')

results = query.stream()

for result in results:
    print(u'{} => {}'.format(result.id, result.to_dict()))
# [END string_contains_METHOD]

# [START boolean_contains_METHOD]
# ./cloud-client-library-code-snippets/python/keyword/boolean_contains_METHOD.py
import sys, threading
