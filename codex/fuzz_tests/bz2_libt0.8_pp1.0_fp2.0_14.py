import bz2
bz2file = bz2.BZ2File('test.json.bz2', 'w')
bz2file.write(gzip.compress(bytes(json.dumps(test),"UTF-8")))
bz2file.close()

import bz2
bz2file = bz2.BZ2File('test.json.bz2', 'r')
test = json.loads(gzip.decompress(bz2file.read()))
bz2file.close()

from datapackage import Package
from datapackage import Resource
import csv
import pandas as pd
from datapackage import Package

def pandas_to_datapackage(df,dst_folio,dst_path,dst_schema,dst_name):
    resource = Resource({'name': dst_name, 'path': dst_path, 'schema':dst_schema})
    resource.infer(df) # Infer the schema from the dataframe
    resource.commit()
    package = Package({'name':
