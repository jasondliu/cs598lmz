import types
types.ClassType

import types
types.InstanceType


import types
types.MethodType


# Importing a Module from a Package

# __init__.py
# import the package
import ibm_db, ibm_db_dbi
# import the module
import ibm_db.test as test

# Importing a Subclass

# __init__.py
# import the package
import ibm_db, ibm_db_dbi
# import the module
import ibm_db.test as test
# import the subclass
import ibm_db.test.my_subclass as my_subclass
# now you can use it
my_subclass.test_connect(conn=conn)

# Importing a Function

# __init__.py
# import the package
import ibm_db, ibm_db_dbi
# import the module
import ibm_db.test as test
# import the function
from ibm_db.test import test_conn_failure
# now you can use it
test_conn_failure(conn=conn)

